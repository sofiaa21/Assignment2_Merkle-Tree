import hashlib
import MerkleTree

if __name__ == "__main__":

    Merkle_Tree_obj = MerkleTree.MerkleTree
    m = "hello"
    hashed_m = Merkle_Tree_obj.init_hash(m)
    print(hashed_m)