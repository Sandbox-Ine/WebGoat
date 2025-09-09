"""
example_issues.py

This file contains intentionally vulnerable code snippets:
1. Debugging / temporary code left in
2. Suspicious / obfuscated dynamic execution
3. Common segmentation fault patterns (C code as string examples)
"""

# --- 1) Debugging / temporary code ---
def calculate_total(items):
    total = sum(items)
    # Debug leftover: printing sensitive info
    print(f"[DEBUG] items={items}, total={total}")
    # Debug breakpoint left in commit
    import pdb; pdb.set_trace()
    return total


# --- 2) Suspicious / potentially malicious patterns ---
import base64

def suspicious_exec():
    # Encoded string -> decoded -> executed
    encoded = "cHJpbnQoIkhpZGRlbiBsb2ciKQ=="  # print("Hidden log")
    decoded = base64.b64decode(encoded).decode()
    exec(decoded)  # BAD: executing decoded string is suspicious


# --- 3) Segmentation fault patterns (C code snippets as string literals) ---
segfault_examples = r"""
// null_deref.c
#include <string.h>
#include <stdio.h>
int main() {
    char *p = NULL;
    printf("%zu\n", strlen(p)); // NULL dereference
}

// use_after_free.c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main() {
    char *p = malloc(10);
    strcpy(p, "hello");
    free(p);
    printf("%s\n", p); // use-after-free
}

// buf_overflow.c
#include <stdio.h>
#include <string.h>
int main() {
    char buf[8];
    strcpy(buf, "too-long-string"); // buffer overflow
    printf("%s\n", buf);
}
"""
