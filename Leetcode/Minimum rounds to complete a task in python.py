class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_counter = collections.Counter(tasks)
        rounds = 0
        for task_id, count in task_counter.items():
            if count == 1:
                return -1
            rounds += ceil(count/3)
        return rounds