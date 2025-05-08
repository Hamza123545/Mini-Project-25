import streamlit as st

st.title("Binary Search")

arr = st.text_input("Enter a sorted list (comma separated):", "1,2,3,4,5")
arr = [int(x) for x in arr.split(",")]
target = st.number_input("Enter a number to search:", min_value=min(arr), max_value=max(arr))

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if st.button("Search"):
    result = binary_search(arr, target)
    if result != -1:
        st.success(f"Element {target} found at index {result}.")
    else:
        st.error("Element not found.")
