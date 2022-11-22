class Node:
    """Node class for future implementation of hashtable using linked list"""
    def __init__(self, key=None, data=None, prev=None, next=None):
        self.data = data
        self.key = key
        self.prev = prev
        self.next = next


class LinkedList:
    """

    LinkedList for future implementation of hashtable

    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        if self.head is None:
            return "Empty Linked List"
        itr = self.head
        listr = ''
        while itr:
            if itr.next is None:
                listr += str(itr.data)
                break
            listr += str(itr.data) + '->'
            itr = itr.next
            return listr

    def insert(self):
        pass

    def get_last_node(self):
        itr = self.head
        # travel down the linked list from the head to the last node via next node
        while itr:
            if itr.next is None:
                return itr
            itr = itr.next

    def traverse_backward(self):
        if self.head is None:
            return "Empty Linked List"
        itr = self.get_last_node()
        listr = ''
        while itr:
            if itr.prev is None:
                listr += str(itr.data)
                break
            listr += str(itr.data) + '->'
            itr = itr.prev
        return listr


class HashTable:
    # MIT 6.006 - table size prime
    table_size = 31  # should not be a power of 2 or a power of 10 and should be prime

    def __init__(self):
        self.buckets = [None for i in range(self.table_size)]
        self.size = 0

    def insert(self, key, item):
        """
        O(n) Time-for bucket traversal O(n) space

        insert item into hashtable and store the item with its key
        :param key:
        :param item:
        :return:
        """
        # identify the bucket for insertion
        index = self.__hash_index__(key)

        # if the bucket is empty append the key/value pair
        if self.buckets[index] is None:
            self.buckets[index] = []

        for i, kv_pair in enumerate(self.buckets[index]):
            k, v = kv_pair
            if k == key:
                # if the key is in the bucket update the key/value pair with the new key/value pair
                self.buckets[index][i] = (key, item)
                return

        self.buckets[index].append((key, item))
        self.size += 1

    def delete(self, key):
        """ NOT IMPLEMENTED"""
        pass

    def search(self, key):
        """
        O(n) Time O(n) Space
        :param key:
        :return:
        """

        hash_key = self.__hash_index__(key)
        bucket = self.buckets[hash_key]
        if bucket is not None:
            for item in bucket:

                if item[0] == key:
                    return item

        return None
        #raise KeyError

    def __hash_index__(self, prekey):
        """
        O(1) Time O(1) Space

        returns a hashed index from the passed prekey
        :param prekey:
        :return:
        """
        # keys are finite and discrete.  covert key to discrete integer

        # expected length of chain for n keys, m slots = n/m = alpha = load_factor
        # constant time if m => theta n
        # running time = O(1 + length of chain) or 1 + theta n

        # use modulo to set size of table
        # MIT 6.006  h(k) = [(a*k) mod 2^w] >> w-r
        # k = key
        # w = 64 bit cpu
        # a = random integer - odd and not close to a power of 2, in between 2^(r-1) and 2^r
        # m = 2^r
        #key = (self.a * hash(prekey) % (2 ** 64)) >> 8 % self.table_size

        key = hash(prekey) % self.table_size
        return key  #

    def __str__(self):
        hashtablestring = ""
        print_packages = []
        for bucket in self.buckets:
            if bucket is not None:
                for item in bucket:
                    k, v = item
                    print_packages.append(v)
        print_packages = sorted(print_packages, key=lambda x: x.id)
        for package in print_packages:
            hashtablestring += str(package) + "\n"
        return hashtablestring

    def __repr__(self):
        return self.__str__()

    @property
    def keys(self):
        """
        O(n) Time O(n) size
        get all the keys and return them
        :return:
        """
        _keys = []
        for i, bucket in enumerate(self.buckets):
            if self.buckets[i] is not None:
                for item in self.buckets[i]:
                    _keys.append(item[0])

        return _keys

    # dunder functions

    def __getitem__(self, key):
        return self.search(key)[1]

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __len__(self):
        """
        O(1) Time
        :return:
        """
        return self.size



