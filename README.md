RL-based Tictactoe AI
=====================
## Agents

* agent_RL : ��ȭ�н��� ������ ������Ʈ
* agent_Base : ����/�̱�� ���� �δ� �񱳿� ������Ʈ
* agent_Human : input�� �޾Ƽ�, ���� ���� ������Ʈ

## Environment

* Tictactoe ���� ȯ���Դϴ�.
* step(action) : action�� �޾Ƽ� �����ϰ� observation�� ��ȯ�մϴ�.
* render() : ���� ���¸� ȭ�鿡 ����մϴ�.
* init()/reset() : ȯ���� �ʱ�ȭ�մϴ�.

## Learning Algorithm

* Table�� �̿��� Temporal-difference learning method�� ����Ͽ����ϴ�.
* �ڰ����� 350 Episode, ���̽����� 150 Episode�� Training�մϴ�.
* 500 Episode���� ���̽��� 100 Episode�� �׽�Ʈ�մϴ�.
* 50000 Episode���� ��ս·� ����մϴ�.

* �н� ��

```
V(s) := V(s) + learning_rate * (V(s') - V(s))
```

* Hyperparameter

```
1. learning rate : 0.4
2. epsilon : 0.08
```

## Reference

* Richard S. Sutton and Andrew G. Barto. (2018). Reinforcement Learning:An Introduction. 
The MIT Press Cambridge, Massachusetts London, England
