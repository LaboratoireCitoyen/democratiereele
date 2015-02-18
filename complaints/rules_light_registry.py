import rules_light


def my_model_or_staff(user, rulename, obj):
    return user.is_staff or user == obj.author


rules_light.registry['complaints.complaint.read'] = True

rules_light.registry['complaints.complaint.create'] = rules_light.is_authenticated

rules_light.registry['complaints.complaint.update'] = my_model_or_staff

rules_light.registry['complaints.complaint.delete'] = rules_light.is_staff

rules_light.registry['complaints.action.read'] = True

rules_light.registry['complaints.action.create'] = rules_light.is_authenticated

rules_light.registry['complaints.action.update'] = my_model_or_staff

rules_light.registry['complaints.action.delete'] = rules_light.is_staff
