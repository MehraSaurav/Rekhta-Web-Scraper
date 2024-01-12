list=['jagjit singh', 'chitra singh', 'talat mahmood', 'begum akhtar', 'pankaj udhas', 'mohammad rafi', 'bhupinder singh', 'talat aziz', 'chandan das', 'hariharan', 'anup jalota', 'farida khanum', 'k l saigal','kundan lal saigal', 'manna dey', 'suraiya', 'mukesh', 'mehdi hassan', 'ghulam ali', 'munni begum', 'nusrat fateh ali khan', 'nayyara noor', 'abida parveen', 'noor jahan', 'amanat ali khan', 'farida khanum', 'iqbal bano']

def singername(desc):
    desc=desc.lower()
    ans = []
    for i in list:
        if i in desc:
            ans += [i.title()]
    if not ans:
        return "Unknown"
    return ", ".join(ans)