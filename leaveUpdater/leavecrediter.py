from leave_balance.models import leavebalance


def credit_leave(self, pk):
    p_l = 0.5
    s_l = 0.8
    emp = leavebalance.objects.get(pk=16)
    p_l += emp.priviledgeLeave
    s_l += emp.sickLeave
    p_l.save()
    s_l.save()
