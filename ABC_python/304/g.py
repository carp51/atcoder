# 遷移確率と報酬を定義します
trans_probs = {
    'theta_1': {
        's1': {'a1': {'s1': 0.6, 's2': 0.4}, 'a2': {'s1': 0.2, 's2': 0.8}},
        's2': {'a1': {'s1': 0.6, 's2': 0.4}, 'a2': {'s1': 0.5, 's2': 0.5}},
    },
    'theta_2': {
        's1': {'a1': {'s1': 0.5, 's2': 0.5}, 'a2': {'s1': 0.6, 's2': 0.4}},
        's2': {'a1': {'s1': 0.6, 's2': 0.4}, 'a2': {'s1': 0.2, 's2': 0.8}},
    }
}

rewards = {
    's1': {'a1': {'s1': 140, 's2': 200}, 'a2': {'s1': 250, 's2': 100}},
    's2': {'a1': {'s1': 150, 's2': 200}, 'a2': {'s1': 150, 's2': 100}},
}

# 各状態について最適な行動を求めます
for theta in ['theta_1', 'theta_2']:
    for s in ['s1', 's2']:
        max_exp_reward, best_action = None, None
        for a in ['a1', 'a2']:
            exp_reward = sum(trans_probs[theta][s][a][s_prime] * rewards[s][a][s_prime] for s_prime in ['s1', 's2'])
            if max_exp_reward is None or exp_reward > max_exp_reward:
                max_exp_reward = exp_reward
                best_action = a
        print(f"For {theta} and initial state {s}, the action that maximizes the expected reward is: {best_action}")
