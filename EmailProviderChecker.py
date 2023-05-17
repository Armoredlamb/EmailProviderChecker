import dns.resolver

def check_mx_records(domain):
    mx_records = dns.resolver.resolve(domain, 'MX')
    for mx in mx_records:
        if 'outlook.com' in str(mx.exchange):
            return 'Domain uses M365 Email.'
        elif 'google.com' in str(mx.exchange):
            return 'Domain uses Google Email.'
    
    return None

def check_spf_records(domain):
    spf_records = dns.resolver.resolve(domain, 'TXT')
    for spf in spf_records:
        spf_text = str(spf.strings[0])
        if 'outlook.com' in spf_text and 'google.com' not in spf_text:
            return 'Domain likely uses M365 Email based on SPF Record.'
        elif 'google.com' in spf_text and 'outlook.com' not in spf_text:
            return 'Domain likely uses Google Email based on SPF Record.'
    
    return None

def run_script():
    while True:
        domain = input('Enter a domain name (e.g., example.com): ')
        
        result = check_mx_records(domain)
        if result:
            print(result)
        else:
            result = check_spf_records(domain)
            if result:
                print(result)
            else:
                print('Undetermined mail provider.')
        
        choice = input('Do you want to run the script again? (y/n): ')
        if choice.lower() != 'y':
            break

run_script()
