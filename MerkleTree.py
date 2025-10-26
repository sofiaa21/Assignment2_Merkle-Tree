import hashlib 
import math

LAMBDA_BYTES = 32   # 256 bits

class MerkleTree:        
    def tree_hash(data_bytes):
        hash_obj =  hashlib.shake_256(data_bytes)
        return hash_obj.digest(LAMBDA_BYTES)

    def build_tree(message, salt):
        # convert into bits
        message_bits = len(message) * 8
        lambda_bits = 256

        # If the length of message is smaller or same as lambda 
        # the algorithm simply outputs the message m as the hash
        if message_bits <=lambda_bits:
            return message

        # Define our l
        l = math.log2(len(message)/LAMBDA_BYTES)
        # If l == 0, redefine as l = 1, so we can use the 2**l operation
        if l==0:
            l = 1
        
        estimated_length_bytes = ((2**l) *lambda_bits)//8

        # Define padding
        padding_len_bytes = int(estimated_length_bytes - len(message))
        padding = b'\x00' * padding_len_bytes
        m_prime = message + padding
        # We hash the message blocks
        hashes = [] 
        # How many hashes are there to compute (use hash.ceil to avoid floating errors)
        hashes_count = math.ceil((2**(l-1)))

        for i in range(hashes_count):
            start = i * (2*LAMBDA_BYTES)
            end = start + (2*LAMBDA_BYTES)

            data_block = m_prime[start:end]

            #Add salt to hash input s || data_block
            hash_input = salt + data_block

            hash_i = MerkleTree.tree_hash(hash_input)
            hashes.append(hash_i)
        
        concat_hashes = b''.join(hashes)
        
        # Hash the concatenated message to move to next tree level
        return MerkleTree.build_tree(concat_hashes,salt)


