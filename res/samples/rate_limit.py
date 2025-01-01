with open("payloads/ip.txt", "r+") as file:
    lines = file.readlines()
    first_ip = lines[0].strip()
    # Rotate the IP by moving the first line to the end
    lines = lines[1:] + [first_ip + "\n"]
    # Rewind and write back to the file
    file.seek(0)
    file.writelines(lines)
    file.truncate()
    
request.headers['X-Forwarded-For'] = first_ip
