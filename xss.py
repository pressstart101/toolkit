
import requests
# from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

class XSS():

    def __init__(self):
        self.url = None


    def get_all_forms(self,url):
        """Given a `url`, it returns all forms from the HTML content"""
        soup = bs(requests.get(url).content, "html.parser")
        return soup.find_all("form")



    def get_form_details(self, form):
        """
        This function extracts all possible useful information about an HTML `form`
        """
        details = {}
        # get the form action (target url)
        action = form.attrs.get("action").lower()
        # get the form method (POST, GET, etc.)
        method = form.attrs.get("method", "get").lower()
        # get all the input details such as type and name
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})
        # put everything to the resulting dictionary
        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        return details



    def submit_form(self, form_details, url, value):
        """
        Submits a form given in `form_details`
        Params:
            form_details (list): a dictionary that contain form information
            url (str): the original URL that contain that form
            value (str): this will be replaced to all text and search inputs
        Returns the HTTP Response after form submission
        """
        # construct the full URL (if the url provided in action is relative)
        target_url = urljoin(url, form_details["action"])
        # get the inputs
        inputs = form_details["inputs"]
        data = {}
        for input in inputs:
            # replace all text and search values with `value`
            if input["type"] == "text" or input["type"] == "search":
                input["value"] = value
            input_name = input.get("name")
            input_value = input.get("value")
            if input_name and input_value:
                # if input name and value are not None, 
                # then add them to the data of form submission
                data[input_name] = input_value

        if form_details["method"] == "post":
            return requests.post(target_url, data=data)
        else:
            # GET request
            return requests.get(target_url, params=data)



    def scan_xss(self, url):
        """
        Given a `url`, it prints all XSS vulnerable forms and 
        returns True if any is vulnerable, False otherwise
        """
        # get all the forms from the URL

        forms = self.get_all_forms(url)
        # print(f"[+] Detected {len(forms)} forms on {url}.")
        
        js_script = "<Script>alert('hi')</scripT>"
        # returning value
        is_vulnerable = False
        result = {"url": url,
            "num_of_vulnerable_forms": len(forms),
            "is_vulnerable": is_vulnerable,
            }
        # iterate over all forms
        for form in forms:
            form_details = self.get_form_details(form)
            content = self.submit_form(form_details, url, js_script).content.decode()
            if js_script in content:
                # print(f"[+] XSS Detected on {url}")
                # print(f"[*] Form details:")
                # pprint(form_details)
                # print("\n\n\nform details\n\n\n")
                # print(form_details['inputs'][0]['name'])
                is_vulnerable = True
                field_name = form_details['inputs'][0]['name']
                exploit = form_details['inputs'][0]['value']
                form_type = form_details['inputs'][0]['type']
                method = form_details['method']
                result['exploit'] = exploit
                result['field_name'] = field_name
                result['form_type'] = form_type
                result['method'] = method
                result['is_vulnerable'] = is_vulnerable
                 # won't break because we want to print available vulnerable forms
        return result


# if __name__ == "__main__":
#     url = "https://xss-game.appspot.com/level1/frame"
#     xss = XSS()
#     # xss.get_all_forms(url)
#     print(xss.scan_xss(url))


# jquery.get
# or fetch


