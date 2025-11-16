**d-Value Generator**



**RSA Decryption Key Calculator (Tkinter GUI)**



A lightweight Python tool that computes modular inverses to generate the RSA decryption key d using the condition:



&nbsp;				(e⋅d) mod mod = 1



Built as a simple exploration of asymmetric cryptography concepts.



🚀 **Run the Program**



```bash

python d\_value\_generator.py

```



**Requirements:**



* Python 3



* Tkinter (included with Python)



🧩 **How It Works**



1. Enter **e**
   
2. Enter mod (often φ(n))
   
3. Press **=**
   
4. The program searches for values of d (1–1000 ) that satisfy the modular inverse rule:



&nbsp;				(e⋅d)%mod=1



The resulting d-values appear in the output field.



⚠️ **Disclaimer**



This project is for educational use only.

It is not intended for real-world cryptographic applications.



