# -*- coding: utf-8 -*-
"""sort_object_y.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yho54N1W11pN2PjnSrPbcKt4w-2Z5TgY
"""

obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'pen': [155, 100], 'mouse':
[200, 45], 'remote': [298, 165], 'fan': [300, 36]}

sorted(obj_detected.items(), key=lambda item : item[0], reverse = False )