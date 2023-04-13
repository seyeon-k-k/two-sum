{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yBdLYy0EUUtG",
        "outputId": "587622dc-d38a-45bc-83d2-52ea32f612eb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "220\n"
          ]
        }
      ],
      "source": [
        "from typing import List\n",
        "# Skeleton code for even_list\n",
        "def even_list(int_list: List[int]) -> List[int]:\n",
        "    \"\"\"\n",
        "    Determines if a number is even and return an even list.\n",
        "    Args:        int_list: A list of integer.\n",
        "    Returns:        A list of even integers.\n",
        "    \"\"\"\n",
        "    returnlist = []\n",
        "    # TODO: Implement even_list\n",
        "    for i in int_list:\n",
        "        if i%2 == 0:\n",
        "            returnlist.append(i)\n",
        "    return returnlist\n",
        "\n",
        "# Skeleton code for sum_of_squares_of_even\n",
        "\n",
        "def sum_of_squares_of_even(even_int_list: List[int]) -> int:\n",
        "    \"\"\"\n",
        "    Computes the sum of the squares of all even numbers in a list of integers.\n",
        "    Args:    \n",
        "        even_int_list: A list of even integers.\n",
        "    Returns:\n",
        "        The sum of the squares of all even numbers in the list.\n",
        "    \"\"\"\n",
        "    # TODO: Implement sum_of_squares_of_even\n",
        "    sum = 0\n",
        "    for i in even_int_list:\n",
        "        sum += i**2\n",
        "    return sum\n",
        "# Main function\n",
        "def main():\n",
        "    # Example list\n",
        "    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
        "    even_int_list = even_list(int_list)\n",
        "    output = sum_of_squares_of_even(even_int_list)\n",
        "    print(output)\n",
        "# Boilerplate code\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ]
}