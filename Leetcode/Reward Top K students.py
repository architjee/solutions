from typing import *
class Solution:
    positive_feedback = ["smart","brilliant","studious"], 
    negative_feedback = ["not"], 
    report = ["this student is studious","the student is smart"], 
    student_id = [1,2], 
    k = 2
    ## Output will be [1,2]
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        def calc_points(his_report):
            positive = 0
            negative = 0
            for word in his_report.split(' '):
                if word in positive_feedback:
                    positive+=1
                elif word in negative_feedback:
                    negative+=1
            return positive - negative
        for stud_id in student_id:
            his_repo = report[stud_id-1]
            points= calc_points(his_repo)