pricing = {'tomato': 3, 'cucumber': 2, 'cola': 5, 'chicken': 20}
def groceries():
    inputs = {
        'tomato': int(input('please enter your tomatos amount\n')),
        'cucumber': int(input('please enter your cucumbers amount\n')),
        'cola': int(input('please enter your colas amount\n')),
        'chicken': float(input('please enter your chicken weight in Kg\n'))
    }
    
    total_price = 0
    for key in pricing.keys():
        total_price += pricing[key] * inputs[key]
    total_price = int(total_price * 1.17)
    print(f'your total price is {total_price}\n')

def ips():
    ip_addresses = []
    for i in range(5):
        ip_addresses.append(input(f'please enter ip address number {i+1}\n'))
    
    additional_ip = input('please enter an additional ip address\n')
    if (additional_ip in ip_addresses):
        print("sorry, this ip is already in use")
    else:
        print(f'adding {additional_ip} to the ips list')
        ip_addresses.append(additional_ip)

    print(f'the list has {len(ip_addresses)} addresses, here they are:\n{ip_addresses}')

def urls():
    urls = {}
    for i in range(2):
        # urls[input('please enter a url\n')] = input('please enter the url\'s ip address\n')
        urls[i] = {'url': input('please enter a url\n'), 'ip': input('please enter the url\'s ip address\n')}
    
    update_message = 'please enter the updated ip address for ' + urls[1]['ip'] + '\n'
    urls[1]['ip'] = input(update_message)

    for url in urls:
        # print(url)
        if (urls[url]['url'] == 'www.google.com'):
            print(urls[url]['ip'])
            break
    
    url_2_delete = input('please enter the url for deletion\n')
    for url in urls:
        if (urls[url]['url'] == url_2_delete):
            del urls[url]
            break
    print(urls)

if __name__ == "__main__":
    groceries()
    ips()
    urls()