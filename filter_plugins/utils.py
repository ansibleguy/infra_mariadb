from re import sub as regex_replace


class FilterModule(object):

    def filters(self):
        return {
            "safe_key": self.safe_key,
            "mgmt_pwd": self.mgmt_pwd,
        }

    @staticmethod
    def safe_key(key: str) -> str:
        return regex_replace('[^0-9a-zA-Z]+', '', key.replace(' ', '_'))

    def mgmt_pwd(self, instance: dict) -> str:
        return self.fallback(opt1=instance['ansible_pwd'], opt2=instance['root_pwd'])

    @staticmethod
    def fallback(opt1: str, opt2: str) -> str:
        if opt1 not in [None, '', 'None', 'none', ' ']:
            return opt1

        return opt2
