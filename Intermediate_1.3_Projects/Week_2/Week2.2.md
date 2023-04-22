{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1msyxbUCyBH4bq10KkaJDb2rdu_njlfMv",
      "authorship_tag": "ABX9TyMqxFSLbb0TWmCn6dJ7dcJ3",
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
        "<a href=\"https://colab.research.google.com/github/Esther-EA/Stutern_Projects/blob/master/Intermediate_1.3_Projects/Week_2/Week2.2.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MkK19XRk_0G5"
      },
      "outputs": [],
      "source": [
        "from google.colab import drive"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/drive/MyDrive/intermediate_1.3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZfYwu9zvAC1P",
        "outputId": "9b58b7bb-5d5e-4756-b3b1-988efc3c934d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/intermediate_1.3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd \n",
        "import psycopg2 as ps\n",
        "import psycopg2.extras\n",
        "import sqlalchemy\n",
        "from sqlalchemy import create_engine\n",
        "# import connection"
      ],
      "metadata": {
        "id": "VvRym0QqxX6x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# create a connection \n",
        "\n",
        "engine= create_engine(\"postgresql+psycopg2://postgres:datafreak@localhost:5432/demo_db\", pool_recycle =-1)\n",
        "\n",
        "# db = engine.connect()\n",
        "\n",
        "# postgresql+psycopg2://USERNAME:PASSWORD@HOSTNAME:PORT/DATABASE\""
      ],
      "metadata": {
        "id": "ap2HGRXV8qD1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "query = \"SELECT * FROM scores_waec\" "
      ],
      "metadata": {
        "id": "F3kyo6bVONlh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data = pd.read_sql_query(query, engine)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 694
        },
        "id": "LpTK6k5LOi7G",
        "outputId": "900461ed-a418-44b9-a144-bb1502749c03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "OperationalError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/base.py\u001b[0m in \u001b[0;36m_wrap_pool_connect\u001b[0;34m(self, fn, connection)\u001b[0m\n\u001b[1;32m   3360\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3361\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3362\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mdialect\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    326\u001b[0m         \"\"\"\n\u001b[0;32m--> 327\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_ConnectionFairy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_checkout\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    328\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m_checkout\u001b[0;34m(cls, pool, threadconns, fairy)\u001b[0m\n\u001b[1;32m    893\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mfairy\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 894\u001b[0;31m             \u001b[0mfairy\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_ConnectionRecord\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheckout\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpool\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    895\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36mcheckout\u001b[0;34m(cls, pool)\u001b[0m\n\u001b[1;32m    492\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mcheckout\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 493\u001b[0;31m         \u001b[0mrec\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_do_get\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    494\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/impl.py\u001b[0m in \u001b[0;36m_do_get\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    145\u001b[0m                 \u001b[0;32mwith\u001b[0m \u001b[0mutil\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msafe_reraise\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 146\u001b[0;31m                     \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_dec_overflow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    147\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/langhelpers.py\u001b[0m in \u001b[0;36m__exit__\u001b[0;34m(self, type_, value, traceback)\u001b[0m\n\u001b[1;32m     69\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarn_only\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 70\u001b[0;31m                 compat.raise_(\n\u001b[0m\u001b[1;32m     71\u001b[0m                     \u001b[0mexc_value\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/compat.py\u001b[0m in \u001b[0;36mraise_\u001b[0;34m(***failed resolving arguments***)\u001b[0m\n\u001b[1;32m    210\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 211\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    212\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/impl.py\u001b[0m in \u001b[0;36m_do_get\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    142\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 143\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_create_connection\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    144\u001b[0m             \u001b[0;32mexcept\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m_create_connection\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    272\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 273\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_ConnectionRecord\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    274\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, pool, connect)\u001b[0m\n\u001b[1;32m    387\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mconnect\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 388\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__connect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    389\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfinalize_callback\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdeque\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m__connect\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    690\u001b[0m             \u001b[0;32mwith\u001b[0m \u001b[0mutil\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msafe_reraise\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 691\u001b[0;31m                 \u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Error on connect(): %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    692\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/langhelpers.py\u001b[0m in \u001b[0;36m__exit__\u001b[0;34m(self, type_, value, traceback)\u001b[0m\n\u001b[1;32m     69\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarn_only\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 70\u001b[0;31m                 compat.raise_(\n\u001b[0m\u001b[1;32m     71\u001b[0m                     \u001b[0mexc_value\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/compat.py\u001b[0m in \u001b[0;36mraise_\u001b[0;34m(***failed resolving arguments***)\u001b[0m\n\u001b[1;32m    210\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 211\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    212\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m__connect\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    685\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstarttime\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 686\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdbapi_connection\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconnection\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_invoke_creator\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    687\u001b[0m             \u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Created new connection %r\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconnection\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/create.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(connection_record)\u001b[0m\n\u001b[1;32m    573\u001b[0m                         \u001b[0;32mreturn\u001b[0m \u001b[0mconnection\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 574\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mdialect\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    575\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/default.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(self, *cargs, **cparams)\u001b[0m\n\u001b[1;32m    597\u001b[0m         \u001b[0;31m# inherits the docstring from interfaces.Dialect.connect\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 598\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    599\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/psycopg2/__init__.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(dsn, connection_factory, cursor_factory, **kwargs)\u001b[0m\n\u001b[1;32m    121\u001b[0m     \u001b[0mdsn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_ext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmake_dsn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdsn\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 122\u001b[0;31m     \u001b[0mconn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_connect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdsn\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconnection_factory\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mconnection_factory\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwasync\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    123\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcursor_factory\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mOperationalError\u001b[0m: could not connect to server: Connection refused\n\tIs the server running on host \"localhost\" (127.0.0.1) and accepting\n\tTCP/IP connections on port 5432?\ncould not connect to server: Cannot assign requested address\n\tIs the server running on host \"localhost\" (::1) and accepting\n\tTCP/IP connections on port 5432?\n",
            "\nThe above exception was the direct cause of the following exception:\n",
            "\u001b[0;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-18-d92313b62ad9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_sql_query\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/pandas/io/sql.py\u001b[0m in \u001b[0;36mread_sql_query\u001b[0;34m(sql, con, index_col, coerce_float, params, parse_dates, chunksize, dtype)\u001b[0m\n\u001b[1;32m    398\u001b[0m     \"\"\"\n\u001b[1;32m    399\u001b[0m     \u001b[0mpandas_sql\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpandasSQL_builder\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcon\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 400\u001b[0;31m     return pandas_sql.read_query(\n\u001b[0m\u001b[1;32m    401\u001b[0m         \u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    402\u001b[0m         \u001b[0mindex_col\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mindex_col\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/pandas/io/sql.py\u001b[0m in \u001b[0;36mread_query\u001b[0;34m(self, sql, index_col, coerce_float, parse_dates, params, chunksize, dtype)\u001b[0m\n\u001b[1;32m   1558\u001b[0m         \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_convert_params\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1559\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1560\u001b[0;31m         \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1561\u001b[0m         \u001b[0mcolumns\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkeys\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1562\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/pandas/io/sql.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1403\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1404\u001b[0m         \u001b[0;34m\"\"\"Simple passthrough to SQLAlchemy connectable\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1405\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnectable\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecution_options\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1406\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1407\u001b[0m     def read_table(\n",
            "\u001b[0;32m<string>\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, statement, *multiparams, **params)\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/deprecations.py\u001b[0m in \u001b[0;36mwarned\u001b[0;34m(fn, *args, **kwargs)\u001b[0m\n\u001b[1;32m    466\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mskip_warning\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    467\u001b[0m             \u001b[0m_warn_with_version\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mversion\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwtype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacklevel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 468\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    469\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    470\u001b[0m     \u001b[0mdoc\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/base.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, statement, *multiparams, **params)\u001b[0m\n\u001b[1;32m   3254\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3255\u001b[0m         \"\"\"\n\u001b[0;32m-> 3256\u001b[0;31m         \u001b[0mconnection\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mclose_with_result\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3257\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mconnection\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstatement\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mmultiparams\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3258\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/base.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(self, close_with_result)\u001b[0m\n\u001b[1;32m   3313\u001b[0m         \"\"\"\n\u001b[1;32m   3314\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3315\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_connection_cls\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclose_with_result\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mclose_with_result\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3316\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3317\u001b[0m     @util.deprecated(\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/base.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, engine, connection, close_with_result, _branch_from, _execution_options, _dispatch, _has_events, _allow_revalidate)\u001b[0m\n\u001b[1;32m     94\u001b[0m                 \u001b[0mconnection\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     95\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mconnection\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 96\u001b[0;31m                 \u001b[0;32melse\u001b[0m \u001b[0mengine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mraw_connection\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     97\u001b[0m             )\n\u001b[1;32m     98\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/base.py\u001b[0m in \u001b[0;36mraw_connection\u001b[0;34m(self, _connection)\u001b[0m\n\u001b[1;32m   3392\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3393\u001b[0m         \"\"\"\n\u001b[0;32m-> 3394\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_wrap_pool_connect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_connection\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3396\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/base.py\u001b[0m in \u001b[0;36m_wrap_pool_connect\u001b[0;34m(self, fn, connection)\u001b[0m\n\u001b[1;32m   3362\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mdialect\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3363\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mconnection\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3364\u001b[0;31m                 Connection._handle_dbapi_exception_noconnection(\n\u001b[0m\u001b[1;32m   3365\u001b[0m                     \u001b[0me\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdialect\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3366\u001b[0m                 )\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/base.py\u001b[0m in \u001b[0;36m_handle_dbapi_exception_noconnection\u001b[0;34m(cls, e, dialect, engine)\u001b[0m\n\u001b[1;32m   2196\u001b[0m             \u001b[0mutil\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mraise_\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnewraise\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwith_traceback\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfrom_\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2197\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mshould_wrap\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2198\u001b[0;31m             util.raise_(\n\u001b[0m\u001b[1;32m   2199\u001b[0m                 \u001b[0msqlalchemy_exception\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwith_traceback\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfrom_\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2200\u001b[0m             )\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/compat.py\u001b[0m in \u001b[0;36mraise_\u001b[0;34m(***failed resolving arguments***)\u001b[0m\n\u001b[1;32m    209\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    210\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 211\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    212\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    213\u001b[0m             \u001b[0;31m# credit to\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/base.py\u001b[0m in \u001b[0;36m_wrap_pool_connect\u001b[0;34m(self, fn, connection)\u001b[0m\n\u001b[1;32m   3359\u001b[0m         \u001b[0mdialect\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdialect\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3360\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3361\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3362\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mdialect\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3363\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mconnection\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    325\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    326\u001b[0m         \"\"\"\n\u001b[0;32m--> 327\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_ConnectionFairy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_checkout\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    328\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    329\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_return_conn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrecord\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m_checkout\u001b[0;34m(cls, pool, threadconns, fairy)\u001b[0m\n\u001b[1;32m    892\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_checkout\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mthreadconns\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfairy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    893\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mfairy\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 894\u001b[0;31m             \u001b[0mfairy\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_ConnectionRecord\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheckout\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpool\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    895\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    896\u001b[0m             \u001b[0mfairy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_pool\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36mcheckout\u001b[0;34m(cls, pool)\u001b[0m\n\u001b[1;32m    491\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mclassmethod\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    492\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mcheckout\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 493\u001b[0;31m         \u001b[0mrec\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_do_get\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    494\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    495\u001b[0m             \u001b[0mdbapi_connection\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mrec\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_connection\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/impl.py\u001b[0m in \u001b[0;36m_do_get\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    144\u001b[0m             \u001b[0;32mexcept\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    145\u001b[0m                 \u001b[0;32mwith\u001b[0m \u001b[0mutil\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msafe_reraise\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 146\u001b[0;31m                     \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_dec_overflow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    147\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    148\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_do_get\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/langhelpers.py\u001b[0m in \u001b[0;36m__exit__\u001b[0;34m(self, type_, value, traceback)\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_exc_info\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m  \u001b[0;31m# remove potential circular references\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     69\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarn_only\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 70\u001b[0;31m                 compat.raise_(\n\u001b[0m\u001b[1;32m     71\u001b[0m                     \u001b[0mexc_value\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     72\u001b[0m                     \u001b[0mwith_traceback\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexc_tb\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/compat.py\u001b[0m in \u001b[0;36mraise_\u001b[0;34m(***failed resolving arguments***)\u001b[0m\n\u001b[1;32m    209\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    210\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 211\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    212\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    213\u001b[0m             \u001b[0;31m# credit to\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/impl.py\u001b[0m in \u001b[0;36m_do_get\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    141\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_inc_overflow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    142\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 143\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_create_connection\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    144\u001b[0m             \u001b[0;32mexcept\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    145\u001b[0m                 \u001b[0;32mwith\u001b[0m \u001b[0mutil\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msafe_reraise\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m_create_connection\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    271\u001b[0m         \u001b[0;34m\"\"\"Called by subclasses to create a new ConnectionRecord.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    272\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 273\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_ConnectionRecord\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    274\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    275\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_invalidate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconnection\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_checkin\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, pool, connect)\u001b[0m\n\u001b[1;32m    386\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__pool\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    387\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mconnect\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 388\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__connect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    389\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfinalize_callback\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdeque\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    390\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m__connect\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    689\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mBaseException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    690\u001b[0m             \u001b[0;32mwith\u001b[0m \u001b[0mutil\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msafe_reraise\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 691\u001b[0;31m                 \u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Error on connect(): %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    692\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    693\u001b[0m             \u001b[0;31m# in SQLAlchemy 1.4 the first_connect event is not used by\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/langhelpers.py\u001b[0m in \u001b[0;36m__exit__\u001b[0;34m(self, type_, value, traceback)\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_exc_info\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m  \u001b[0;31m# remove potential circular references\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     69\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarn_only\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 70\u001b[0;31m                 compat.raise_(\n\u001b[0m\u001b[1;32m     71\u001b[0m                     \u001b[0mexc_value\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     72\u001b[0m                     \u001b[0mwith_traceback\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexc_tb\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/util/compat.py\u001b[0m in \u001b[0;36mraise_\u001b[0;34m(***failed resolving arguments***)\u001b[0m\n\u001b[1;32m    209\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    210\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 211\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    212\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    213\u001b[0m             \u001b[0;31m# credit to\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/pool/base.py\u001b[0m in \u001b[0;36m__connect\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    684\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    685\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstarttime\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 686\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdbapi_connection\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconnection\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_invoke_creator\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    687\u001b[0m             \u001b[0mpool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Created new connection %r\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconnection\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    688\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfresh\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/create.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(connection_record)\u001b[0m\n\u001b[1;32m    572\u001b[0m                     \u001b[0;32mif\u001b[0m \u001b[0mconnection\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    573\u001b[0m                         \u001b[0;32mreturn\u001b[0m \u001b[0mconnection\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 574\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mdialect\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    575\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    576\u001b[0m         \u001b[0mcreator\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpop_kwarg\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"creator\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconnect\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/sqlalchemy/engine/default.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(self, *cargs, **cparams)\u001b[0m\n\u001b[1;32m    596\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    597\u001b[0m         \u001b[0;31m# inherits the docstring from interfaces.Dialect.connect\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 598\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    599\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    600\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mcreate_connect_args\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/psycopg2/__init__.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(dsn, connection_factory, cursor_factory, **kwargs)\u001b[0m\n\u001b[1;32m    120\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    121\u001b[0m     \u001b[0mdsn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_ext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmake_dsn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdsn\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 122\u001b[0;31m     \u001b[0mconn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_connect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdsn\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconnection_factory\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mconnection_factory\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwasync\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    123\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcursor_factory\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcursor_factory\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcursor_factory\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mOperationalError\u001b[0m: (psycopg2.OperationalError) could not connect to server: Connection refused\n\tIs the server running on host \"localhost\" (127.0.0.1) and accepting\n\tTCP/IP connections on port 5432?\ncould not connect to server: Cannot assign requested address\n\tIs the server running on host \"localhost\" (::1) and accepting\n\tTCP/IP connections on port 5432?\n\n(Background on this error at: https://sqlalche.me/e/14/e3q8)"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd \n",
        "import psycopg2 as ps\n",
        "import psycopg2.extras\n",
        "import sqlalchemy\n",
        "from sqlalchemy import create_engine"
      ],
      "metadata": {
        "id": "C2z4Yx9kQoWU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# create a connection \n",
        "engine= create_engine(\"postgresql+psycopg2://postgres:datafreak@localhost:5432/project\", pool_recycle =-1)"
      ],
      "metadata": {
        "id": "p6hf-aVjQoqS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# create column using list \n",
        "column =[\n",
        "\"course_id\",\n",
        "\"course_title\",\n",
        "\"url\",\n",
        "\"is_paid\",\n",
        "\"price\",\n",
        "\"num_subscribers\",\n",
        "\"num_reviews\",\n",
        "\"num_lectures\",\n",
        "\"level\",\n",
        "\"content_duration\",\n",
        "\"published_timestamp\",\n",
        "\"subject\"]"
      ],
      "metadata": {
        "id": "HPH3g2iGQov1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data = pd.read_csv(r\"C:\\Users\\esthe\\Downloads\\udemy_courses.csv\", names = column)"
      ],
      "metadata": {
        "id": "mVXTU-XNQo3L"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# query the data \n",
        "query = \"SELECT * FROM udemy_courses\""
      ],
      "metadata": {
        "id": "zxF3V_sGQ4DL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# create variable to house database\n",
        "data = pd.read_sql_query(query, engine)"
      ],
      "metadata": {
        "id": "jwff83-zQ4Gq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# read data1 to sql database\n",
        "data.to_sql(\"udemy_courses\", engine, index= False) "
      ],
      "metadata": {
        "id": "9wIWEbuoRE6p"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "QW6V7PuoRFBH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "DdKjfzJkQ4MI"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}