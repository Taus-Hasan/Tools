import socket
import requests

def analyze_ip_address(ip_address):
    try:
        # Get the hostname for the IP address
        hostname = socket.gethostbyaddr(ip_address)[0]
        print(f'Hostname: {hostname}')

        # Get the IP address's physical location using an external API
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()

        # Extract relevant information from the API response
        country = data['country']
        region = data['regionName']
        city = data['city']
        zip_code = data['zip']
        timezone = data['timezone']
        isp = data['isp']
        organization = data['org']
        as_number = data['as']

        # Print the IP address's location information
        print(f'Country: {country}')
        print(f'Region: {region}')
        print(f'City: {city}')
        print(f'ZIP Code: {zip_code}')
        print(f'Timezone: {timezone}')
        print(f'ISP: {isp}')
        print(f'Organization: {organization}')
        print(f'AS Number: {as_number}')

    except socket.herror as e:
        print(f'Error: Unable to resolve hostname for IP address - {str(e)}')

    except requests.RequestException as e:
        print(f'Error: Unable to fetch IP location - {str(e)}')

# Example usage
ip_address = '8.8.8.8'
analyze_ip_address(ip_address)
