import MerkleTree
import os

message = b' In the book it said: "Boa constrictors swallow their prey whole, without chewing it. After that they are not able to move, and they sleep through the six months that they need for digestion.'

# Salt A
salt_a = os.urandom(32)
# Salt B
salt_b = os.urandom(32)

merkle_tree = MerkleTree.MerkleTree
hash_a = merkle_tree.build_tree(message, salt_a)
hash_b = merkle_tree.build_tree(message, salt_b)

# The final hashes MUST be different
assert hash_a != hash_b
print(f"This is hashed value of message m with salt A: {hash_a} with length: {len(hash_a)} bytes")
print(f"This is hashed value of message m with salt B: {hash_b} with length: {len(hash_b)} bytes")

