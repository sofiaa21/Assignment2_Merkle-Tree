import hashlib 

LAMBDA = 256
class MerkleTree:
    def init_hash(message_leaf):
        return hashlib.shake_256(message_leaf.encode("utf-8")).hexdigest(LAMBDA)



