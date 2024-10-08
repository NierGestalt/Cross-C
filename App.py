{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOtgw5Z8Pnra0cS6pHq6Oym",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/NierGestalt/Cross-C/blob/master/App.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "# Title of the app\n",
        "st.title('Interactive Sales Data Visualization App')\n",
        "\n",
        "# Pre-loaded dataset for sales information\n",
        "data = {\n",
        "    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],\n",
        "        'Sales (Thousands USD)': [150, 200, 300, 400, 250],\n",
        "            'Quantity Sold': [30, 45, 55, 65, 50]\n",
        "        }\n",
        "            df = pd.DataFrame(data)\n",
        "\n",
        "            # Display the dataset\n",
        "            st.write(\"Sales Data:\")\n",
        "            st.write(df)\n",
        "\n",
        "            # Let the user select columns for the chart\n",
        "            columns = df.columns.tolist()\n",
        "\n",
        "            # Dropdowns for X and Y axes selection\n",
        "            x_axis = st.selectbox('Select column for X-axis', columns)\n",
        "            y_axis = st.selectbox('Select column for Y-axis', columns)\n",
        "\n",
        "            # Choose chart type: Bar Chart or Line Chart\n",
        "            chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])\n",
        "\n",
        "            # Display chart based on user selections\n",
        "            if chart_type == 'Bar Chart':\n",
        "                st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))\n",
        "                elif chart_type == 'Line Chart':\n",
        "                    st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "oIcYl1EX00DD",
        "outputId": "fbd85fbc-81ad-469a-e10f-c24491ca67b5"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "unexpected indent (<ipython-input-2-db5a817d8432>, line 12)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-2-db5a817d8432>\"\u001b[0;36m, line \u001b[0;32m12\u001b[0m\n\u001b[0;31m    df = pd.DataFrame(data)\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
          ]
        }
      ]
    }
  ]
}