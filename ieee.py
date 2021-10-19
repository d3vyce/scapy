IEEE_FILENAME = "ieee-oui.txt"

class IEEEParser():

    def __init__(self):
        self.db = {}
        self._load_database(1024)

    def _load_database(self, maxsize):
        """
        OPEN IEEE_FILENAME
        And save each entry in a dictionary (self.db) with
        mac prefix as key
        constructor as value
        """

        with open(IEEE_FILENAME) as ieee_file:
            for line in ieee_file:
                if (line[0] == '#'): continue
                result = line.split('\t')
                mac = result[0]
                vendor = result[1].strip()
                self.db[mac] = vendor

    def search_constructor(self, mac):
        """
        Find the mac address in database and return the result

        :param mac: MAC address to find (ex: "00:11:22:33:44:55", "012345abcdef")
        :return: Constructor or None if not found
        """

        mac = mac.replace(":", "").upper()[:6]

        if mac in self.db: return self.db[mac]
        return None

