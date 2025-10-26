import MerkleTree
import os

if __name__ == "__main__":

    Merkle_Tree_obj = MerkleTree.MerkleTree
    m = "Once when I was six years old I saw a magnificent picture in a book, called True Stories from Nature, about the primeval forest. It was a picture of a boa constrictor in the act of swallowing an animal. Here is a copy of the drawing."
    m_bytes = m.encode('utf-8')
    
    print(f"Original message: {m}")
    print(f"Message length: {len(m)} bytes")

    # Generate random 32 byte string of bytes
    salt = os.urandom(32)
    print(f"Salt that will be used in the Merkle tree (HEX): {salt.hex()}")
    print("------------------------------------------------")
    
    try:
        final_hash = Merkle_Tree_obj.build_tree(m_bytes,salt)
        print(f"Final Merkle Root: {final_hash.hex()}")
        print(f"Hash length: {len(final_hash)} bytes")
    except ValueError as e:
        print(f"Error: {e}")
        print("Please ensure your salt is exactly 32 bytes long.")

    print("----------------------------------------------------------------")