{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8240ebd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n",
      "55\n",
      "89\n",
      "144\n",
      "233\n",
      "377\n",
      "610\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "\n",
    "def fib(n):\n",
    "    \n",
    "    a=0\n",
    "    b=1\n",
    "    print(a)\n",
    "    print(b)\n",
    "    \n",
    "    for i in range(2,n):\n",
    "        c= a+b\n",
    "        a=b\n",
    "        b=c\n",
    "        print(a+b)\n",
    "    \n",
    "fib(15)\n",
    "    \n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0230103",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
