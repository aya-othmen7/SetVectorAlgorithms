def dot_product(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

# orthogonal_check.py
def check_orthogonal_pairs(vector_pairs):
    for i, (v1, v2) in enumerate(vector_pairs):
        ps = dot_product(v1, v2)
        if ps == 0:
            print(f"Vectors {i} are orthogonal")
        else:
            print(f"Vectors {i} are not orthogonal")

# test_dot_product.py
def test_dot_product():
    vector_pairs = [([1, 0], [0, 1]), ([1, 1], [1, 1])]
    check_orthogonal_pairs(vector_pairs)
    # Expected output:
    # Vectors 0 are orthogonal
    # Vectors 1 are not orthogonal

if __name__ == "__main__":
    test_dot_product()