def domain_name(url):
    print(url)
    print(url.split("."))
    url_dot_split = url.split(".")
    if url_dot_split[0] == "www":
        return url_dot_split[1]
    elif(url_dot_split[0].startswith("http") and url_dot_split[0].endswith("www")):
        return url_dot_split[1]
    elif(url_dot_split[0].startswith("http")):
        return url_dot_split[0].split("//")[1]
    else:
        return url_dot_split[
