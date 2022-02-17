import pandas as pd
pd.set_option('display.max_rows', 1000)

employees = pd.read_csv('data/OktaPasswordHealth.csv')
print(employees.columns)

employees.drop(columns=[
    'Activation Date',
    'Authentication Source',
    'Last Login',
    'Last Password Change'], inplace=True)

print(employees.columns) #check

mfa_enrolled = pd.read_csv('data/MFAEnrollmentReport.csv')
print(mfa_enrolled.columns)
mfa_enrolled.drop(columns=[
    'Last Enrolled', 'Last Enrolled_ISO8601', 'Last Used', 'Last Used_ISO8601'],
    inplace=True) #reducing columns to view easier

print(mfa_enrolled.columns) #check columns
filt3 = (mfa_enrolled['User'] == 'Davinder Singh')
print(mfa_enrolled[filt3])

print(mfa_enrolled)

mfa_enrolled_list = [mfa_enrolled.columns.values.tolist()] + \
                    mfa_enrolled.values.tolist() #make df _mfa_enrolled_list into mutable list

print(mfa_enrolled_list) #mutable list of users currently enrolled in MFA
filt1 = employees['Status'].str.contains('DEPROVISIONED', na=False) #removing 'deprovisioned' employee accounts
filt2 = employees['Status'].str.contains('ACTIVE', na=False)

print(employees[filt2])
employees = employees.drop(index=employees[filt1].index)

active_employees = [employees.columns.values.tolist()] + \
                   employees.values.tolist() #make df employees into mutable list

print(active_employees)
print(mfa_enrolled_list)

final_list = active_employees + mfa_enrolled_list
print(final_list)

f = "{:<8}|{:<15}" # formatting

for i in final_list:
    print(f.format(*i))
    