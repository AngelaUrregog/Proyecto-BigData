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
      "cell_type": "markdown",
      "source": [
        "# Taller 1 - WebScraping y MongoDB\n"
      ],
      "metadata": {
        "id": "tHApgJCpMeC7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Habilitar google Drive e instalar librerias\n"
      ],
      "metadata": {
        "id": "3qyDUUIeh0Sp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# habilitamos drive de google desde colab\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ro2GWUEaix6_",
        "outputId": "9c4226a7-9f38-4a5b-812c-49f18f755b53"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install requests beautifulsoup4 lxml"
      ],
      "metadata": {
        "id": "EWKPxjsJNeXl",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 393
        },
        "outputId": "6479c9b1-b5d4-4bdd-b23c-58606f4d554b"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (2.32.4)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.12/dist-packages (4.13.5)\n",
            "Requirement already satisfied: lxml in /usr/local/lib/python3.12/dist-packages (5.4.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests) (3.4.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests) (2025.10.5)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.12/dist-packages (from beautifulsoup4) (2.8)\n",
            "Requirement already satisfied: typing-extensions>=4.0.0 in /usr/local/lib/python3.12/dist-packages (from beautifulsoup4) (4.15.0)\n",
            "\u001b[31mERROR: Operation cancelled by user\u001b[0m\u001b[31m\n",
            "\u001b[0m"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-4148202214.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mget_ipython\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msystem\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'pip install requests beautifulsoup4 lxml'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/google/colab/_shell.py\u001b[0m in \u001b[0;36msystem\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m    150\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    151\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mpip_warn\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 152\u001b[0;31m       \u001b[0m_pip\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprint_previous_import_warning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    153\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    154\u001b[0m   \u001b[0;32mdef\u001b[0m \u001b[0m_send_error\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_content\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/google/colab/_pip.py\u001b[0m in \u001b[0;36mprint_previous_import_warning\u001b[0;34m(output)\u001b[0m\n\u001b[1;32m     54\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mprint_previous_import_warning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     55\u001b[0m   \u001b[0;34m\"\"\"Prints a warning about previously imported packages.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 56\u001b[0;31m   \u001b[0mpackages\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_previously_imported_packages\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     57\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mpackages\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     58\u001b[0m     \u001b[0;31m# display a list of packages using the colab-display-data mimetype, which\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/google/colab/_pip.py\u001b[0m in \u001b[0;36m_previously_imported_packages\u001b[0;34m(pip_output)\u001b[0m\n\u001b[1;32m     48\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0m_previously_imported_packages\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpip_output\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     49\u001b[0m   \u001b[0;34m\"\"\"List all previously imported packages from a pip install.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 50\u001b[0;31m   \u001b[0minstalled\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mset\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_extract_toplevel_packages\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpip_output\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     51\u001b[0m   \u001b[0;32mreturn\u001b[0m \u001b[0msorted\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minstalled\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mintersection\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mset\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmodules\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     52\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/google/colab/_pip.py\u001b[0m in \u001b[0;36m_extract_toplevel_packages\u001b[0;34m(pip_output)\u001b[0m\n\u001b[1;32m     37\u001b[0m   \u001b[0;34m\"\"\"Extract the list of toplevel packages associated with a pip install.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m   \u001b[0mtoplevel\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcollections\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdefaultdict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mset\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 39\u001b[0;31m   \u001b[0;32mfor\u001b[0m \u001b[0mm\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mps\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mimportlib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmetadata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpackages_distributions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     40\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mp\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mps\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     41\u001b[0m       \u001b[0mtoplevel\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mp\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mm\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.12/importlib/metadata/__init__.py\u001b[0m in \u001b[0;36mpackages_distributions\u001b[0;34m()\u001b[0m\n\u001b[1;32m    946\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mdist\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mdistributions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    947\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0mpkg\u001b[0m \u001b[0;32min\u001b[0m \u001b[0m_top_level_declared\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdist\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0m_top_level_inferred\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdist\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 948\u001b[0;31m             \u001b[0mpkg_to_dist\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mpkg\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdist\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmetadata\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Name'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    949\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mdict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpkg_to_dist\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    950\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.12/importlib/metadata/__init__.py\u001b[0m in \u001b[0;36mmetadata\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    442\u001b[0m         \"\"\"\n\u001b[1;32m    443\u001b[0m         opt_text = (\n\u001b[0;32m--> 444\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'METADATA'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    445\u001b[0m             \u001b[0;32mor\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'PKG-INFO'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    446\u001b[0m             \u001b[0;31m# This last clause is here to support old egg-info files.  Its\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.12/importlib/metadata/__init__.py\u001b[0m in \u001b[0;36mread_text\u001b[0;34m(self, filename)\u001b[0m\n\u001b[1;32m    817\u001b[0m             \u001b[0mPermissionError\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    818\u001b[0m         ):\n\u001b[0;32m--> 819\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_path\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjoinpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mencoding\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'utf-8'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    820\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    821\u001b[0m     \u001b[0mread_text\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mDistribution\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_text\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__doc__\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.12/pathlib.py\u001b[0m in \u001b[0;36mread_text\u001b[0;34m(self, encoding, errors)\u001b[0m\n\u001b[1;32m   1025\u001b[0m         \"\"\"\n\u001b[1;32m   1026\u001b[0m         \u001b[0mencoding\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext_encoding\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mencoding\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1027\u001b[0;31m         \u001b[0;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'r'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencoding\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mencoding\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1028\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1029\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.12/pathlib.py\u001b[0m in \u001b[0;36mopen\u001b[0;34m(self, mode, buffering, encoding, errors, newline)\u001b[0m\n\u001b[1;32m   1011\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1012\u001b[0m             \u001b[0mencoding\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext_encoding\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mencoding\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1013\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffering\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencoding\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnewline\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1014\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1015\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mread_bytes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.12/codecs.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, errors)\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 2.Crear DOM inicial"
      ],
      "metadata": {
        "id": "ekK6U-wCkBH-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "url = \"https://www.minjusticia.gov.co/normatividad-co\"\n",
        "response = requests.get(url, verify=False)\n",
        "soup = BeautifulSoup(response.content, 'lxml')\n",
        "\n",
        "container_div = soup.find('div', class_='ms-rtestate-field')\n",
        "\n",
        "# encuentre todos los hypervinculos  dentro del div\n",
        "if container_div:\n",
        "    hyperlinks = container_div.find_all('a')\n",
        "    for link in hyperlinks:\n",
        "        print(link.get('href'))\n",
        "else:\n",
        "    print(\"NO pude encontrar el div\")"
      ],
      "metadata": {
        "id": "nuCSoDF3kG_0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 3.Crear JSON recorriendo el DOM\n"
      ],
      "metadata": {
        "id": "w9akSmkwPoXj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "from urllib.parse import urljoin\n",
        "import urllib3\n",
        "import os\n",
        "import json\n",
        "\n",
        "def extract_links(url):\n",
        "    \"\"\"Extraer enlaces .PDF y .ASPX dentro del dominio de minjusticia.gov.co\"\"\"\n",
        "    try:\n",
        "        response = requests.get(url)\n",
        "        response.raise_for_status()\n",
        "        soup = BeautifulSoup(response.content, 'lxml')\n",
        "\n",
        "        links = []\n",
        "\n",
        "        for a in soup.find_all('a', href=True):\n",
        "            href = a['href']\n",
        "            full_url = urljoin(url, href)\n",
        "\n",
        "            if full_url.startswith(\"https://www.minjusticia.gov.co/normatividad-co/\"):\n",
        "                if full_url.endswith('.pdf'):\n",
        "                    links.append({'url': full_url, 'type': 'pdf'})\n",
        "                elif full_url.endswith('.aspx'):\n",
        "                    links.append({'url': full_url, 'type': 'aspx'})\n",
        "        return links\n",
        "\n",
        "    except requests.exceptions.RequestException as e:\n",
        "        print(f\"Error al acceder a {url}: {e}\")\n",
        "        return []\n",
        "\n",
        "json_file_path = '/content/drive/MyDrive/U Central/Maestria_AnaliticaDeDatos/BigData/minjusticia_links.json'\n",
        "base_url = \"https://www.minjusticia.gov.co/normatividad-co/Paginas/Inicio.aspx\"\n",
        "\n",
        "if os.path.exists(json_file_path):\n",
        "    try:\n",
        "        with open(json_file_path, 'r', encoding='utf-8') as f:\n",
        "            json_data = json.load(f)\n",
        "        all_links = json_data.get(\"links\", [])\n",
        "    except json.JSONDecodeError:\n",
        "        print(\"JSON inválido, iniciando nuevo archivo.\")\n",
        "        all_links = []\n",
        "else:\n",
        "    print(\"No se encontró JSON previo, creando uno nuevo.\")\n",
        "    all_links = []\n",
        "\n",
        "\n",
        "# FILTRAR ENLACES ASPX A VISITAR\n",
        "aspx_links_to_visit = [\n",
        "    link['url'] for link in all_links\n",
        "    if link['type'] == 'aspx' and link['url'].startswith(\"https://www.minjusticia.gov.co/normatividad-co/\")\n",
        "]\n",
        "visited_aspx_links = set()\n",
        "\n",
        "# Limpiar enlaces fuera del dominio\n",
        "all_links = [\n",
        "    link for link in all_links\n",
        "    if link['url'].startswith(\"https://www.minjusticia.gov.co/normatividad-co/\")]\n",
        "\n",
        "while aspx_links_to_visit:\n",
        "    current_aspx_url = aspx_links_to_visit.pop(0)\n",
        "    if current_aspx_url not in visited_aspx_links:\n",
        "        visited_aspx_links.add(current_aspx_url)\n",
        "        print(f\"Visitando: {current_aspx_url}\")\n",
        "\n",
        "        new_links = extract_links(current_aspx_url)\n",
        "\n",
        "        for link in new_links:\n",
        "            if link not in all_links:\n",
        "                all_links.append(link)\n",
        "                if link['type'] == 'aspx':\n",
        "                    aspx_links_to_visit.append(link['url'])\n",
        "\n",
        "\n",
        "# GUARDAR RESULTADOS EN JSON\n",
        "json_output = {\"source_url\": base_url, \"links\": all_links}\n",
        "os.makedirs(os.path.dirname(json_file_path), exist_ok=True)\n",
        "\n",
        "with open(json_file_path, 'w', encoding='utf-8') as f:\n",
        "    json.dump(json_output, f, indent=4, ensure_ascii=False)\n",
        "\n",
        "print(\"Extracción finalizada\")\n",
        "print(f\"Archivo guardado en: {json_file_path}\")"
      ],
      "metadata": {
        "id": "86hbY-FKT8kM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 4.recorrer el JSON y descargar todos los PDF"
      ],
      "metadata": {
        "id": "mRR5Db9UdIV0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "import requests\n",
        "import os\n",
        "\n",
        "# Define the directory to save PDFs\n",
        "pdf_dir = \"/content/drive/MyDrive/U Central/Maestria_AnaliticaDeDatos/BigData/minjusticia_links_PDF\"\n",
        "os.makedirs(pdf_dir, exist_ok=True)\n",
        "\n",
        "# Load the JSON file\n",
        "json_file_path = '/content/drive/MyDrive/U Central/Maestria_AnaliticaDeDatos/BigData/minjusticia_links.json'\n",
        "try:\n",
        "    with open(json_file_path, 'r') as f:\n",
        "        json_data = json.load(f)\n",
        "    all_links = json_data.get(\"links\", [])\n",
        "except FileNotFoundError:\n",
        "    print(f\"Error: {json_file_path} No se encontro.\")\n",
        "    all_links = []\n",
        "except json.JSONDecodeError:\n",
        "    print(f\"Error: {json_file_path} JSON invalido.\")\n",
        "    all_links = []\n",
        "\n",
        "\n",
        "# Download PDF files\n",
        "for link in all_links:\n",
        "    if link['type'] == 'pdf':\n",
        "        pdf_url = link['url']\n",
        "        try:\n",
        "            response = requests.get(pdf_url, stream=True)\n",
        "            response.raise_for_status()\n",
        "\n",
        "            # Extract filename from the URL\n",
        "            filename = os.path.join(pdf_dir, pdf_url.split('/')[-1])\n",
        "\n",
        "            with open(filename, 'wb') as pdf_file:\n",
        "                for chunk in response.iter_content(chunk_size=8192):\n",
        "                    pdf_file.write(chunk)\n",
        "            print(f\"Downloaded: {filename}\")\n",
        "\n",
        "        except requests.exceptions.RequestException as e:\n",
        "            print(f\"Error de descarga {pdf_url}: {e}\")\n",
        "        except Exception as e:\n",
        "            print(f\"Error {pdf_url}: {e}\")\n",
        "\n",
        "print(\"Archivos PDFs descargados.\")"
      ],
      "metadata": {
        "id": "Ug8y3ODSdVZj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 5.Extraer texto de los PDF's y generar un JSON por cada PDF"
      ],
      "metadata": {
        "id": "n97Xzrr7o7C1"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 5.1 Instalar librerías para hacer OCR sobre archivos pdf para extraer texto en español"
      ],
      "metadata": {
        "id": "vWYXtNXcpPoW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Instalando Tesseract OCR y el paquete de ESPAÑOL\n",
        "!apt-get update\n",
        "!apt-get install tesseract-ocr libtesseract-dev tesseract-ocr-spa\n",
        "# Instalar pytesseract and Pillow\n",
        "!pip install pytesseract Pillow\n",
        "!pip install matplotlib-venn\n",
        "!pip install pdfminer.six pdf2image\n",
        "!apt-get install poppler-utils"
      ],
      "metadata": {
        "id": "61Qo5Rw5o_vt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 5.2 Extraer texto de cada PDF descargado y generar un JSON"
      ],
      "metadata": {
        "id": "HLCrTF5irab1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import json\n",
        "import pytesseract\n",
        "from PIL import Image\n",
        "from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter\n",
        "from pdfminer.converter import TextConverter\n",
        "from pdfminer.layout import LAParams\n",
        "from pdfminer.pdfpage import PDFPage\n",
        "from io import StringIO\n",
        "from datetime import datetime\n",
        "from pdf2image import convert_from_path\n",
        "\n",
        "\n",
        "def extraer_texto(pdf_path):\n",
        "\n",
        "    try:\n",
        "        rsrcmgr = PDFResourceManager()\n",
        "        retstr = StringIO()\n",
        "        laparams = LAParams()\n",
        "        device = TextConverter(rsrcmgr, retstr, laparams=laparams)\n",
        "        fp = open(pdf_path, 'rb')\n",
        "        interpreter = PDFPageInterpreter(rsrcmgr, device)\n",
        "        for page in PDFPage.get_pages(fp, caching=True, check_extractable=True):\n",
        "            interpreter.process_page(page)\n",
        "        text = retstr.getvalue()\n",
        "        fp.close()\n",
        "        device.close()\n",
        "        retstr.close()\n",
        "\n",
        "        if text.strip():\n",
        "            return text, 'normal', True\n",
        "    except Exception as e:\n",
        "        print(f\"Standard text extraction failed for {pdf_path}: {e}\")\n",
        "\n",
        "    # Si la extracción estándar falló o no produjo texto, intenta con OCR\n",
        "    try:\n",
        "        # Convertir PDF\n",
        "        images = convert_from_path(pdf_path)\n",
        "        ocr_text = \"\"\n",
        "        for i, image in enumerate(images):\n",
        "            ocr_text += pytesseract.image_to_string(image, lang='spa')\n",
        "        if ocr_text.strip():\n",
        "             return ocr_text, 'OCR', True\n",
        "        else:\n",
        "             print(f\"OCR de texto no fue posible {pdf_path}\")\n",
        "             return \"\", 'OCR', False\n",
        "\n",
        "    except Exception as e:\n",
        "        print(f\"OCR text extraction failed for {pdf_path}: {e}\")\n",
        "        return \"\", 'failed', False # Indicate that both methods failed\n",
        "\n",
        "\n",
        "# Define input and output directories\n",
        "pdf_input_dir = '/content/drive/MyDrive/U Central/Maestria_AnaliticaDeDatos/BigData/minjusticia_links_PDF'\n",
        "json_output_dir = '/content/drive/MyDrive/U Central/Maestria_AnaliticaDeDatos/BigData/minjusticia_texto_json'\n",
        "error_log_path = '/content/drive/MyDrive/UniversidadCentral/Maestría_en_Analítica_de_Datos/Bigdata/Ejercicios_de_clase/DataBase/Web_scraping/error_extract_texto.json'\n",
        "\n",
        "os.makedirs(json_output_dir, exist_ok=True)\n",
        "\n",
        "pdf_files = [f for f in os.listdir(pdf_input_dir) if f.endswith('.pdf')]\n",
        "\n",
        "error_files = []\n",
        "\n",
        "for i, pdf_file in enumerate(pdf_files):\n",
        "    pdf_path = os.path.join(pdf_input_dir, pdf_file)\n",
        "    extracted_text, extraction_type, success = extraer_texto(pdf_path)\n",
        "\n",
        "    if success:\n",
        "        # Create JSON data\n",
        "        json_data = {\n",
        "            \"archivo\": pdf_file,\n",
        "            \"fecha\": datetime.now().strftime(\"%Y-%m-%d\"),\n",
        "            \"tipo_extracion\": extraction_type,\n",
        "            \"texto\": extracted_text\n",
        "        }\n",
        "\n",
        "        # Save JSON to file\n",
        "        json_filename = f\"minsalud{i+1}.json\"\n",
        "        json_path = os.path.join(json_output_dir, json_filename)\n",
        "        with open(json_path, 'w', encoding='utf-8') as f:\n",
        "            json.dump(json_data, f, indent=4, ensure_ascii=False)\n",
        "\n",
        "        print(f\" {pdf_file} -> Guardado en {json_filename} ( {extraction_type})\")\n",
        "    else:\n",
        "        error_files.append(pdf_file)\n",
        "        print(f\"Erro extrayendo {pdf_file} (Extraction Type: {extraction_type})\")\n",
        "\n",
        "\n",
        "with open(error_log_path, 'w', encoding='utf-8') as f:\n",
        "    json.dump({\"failed_files\": error_files}, f, indent=4, ensure_ascii=False)\n",
        "\n",
        "print(\"Extracción de texto del PDF y creación del archivo JSON completas.\")\n",
        "print(f\"Error {error_log_path}\")"
      ],
      "metadata": {
        "id": "1ex7oLwqr3Kw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 6. Cargar JSON a MongoAtlas"
      ],
      "metadata": {
        "id": "e5R09Ua41oGu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install \"pymongo[srv]==4.6.3\" --upgrade\n",
        "!pip install py2neo\n",
        "!pip install --upgrade pymongo certifi"
      ],
      "metadata": {
        "id": "7ITEpeEG1w4L"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import json\n",
        "import traceback\n",
        "import certifi\n",
        "from pymongo import MongoClient\n",
        "from pymongo.errors import PyMongoError, ConnectionFailure\n",
        "\n",
        "# Carpeta donde están los archivos JSON\n",
        "json_input_dir = '/content/drive/MyDrive/U Central/Maestria_AnaliticaDeDatos/BigData/minjusticia_texto_json'\n",
        "\n",
        "# URI de conexión (caracteres especiales codificados)\n",
        "mongo_uri = \"mongodb+srv://UrregoANG:2658362Ang%2A%2A@cluster0.krx1hot.mongodb.net/?retryWrites=true&w=majority&tls=true&appName=Cluster0\"\n",
        "\n",
        "# Nombre de la base de datos y colección\n",
        "db_name = \"MinJusticia\"\n",
        "collection_name = \"Normatividad\"\n",
        "\n",
        "# Verificar conexión con MongoDB Atlas\n",
        "print(\"Verificando conexión segura con MongoDB Atlas...\\n\")\n",
        "\n",
        "try:\n",
        "    client = MongoClient(\n",
        "        mongo_uri,\n",
        "        tls=True,\n",
        "        tlsCAFile=certifi.where(),\n",
        "        serverSelectionTimeoutMS=10000,\n",
        "        tlsAllowInvalidCertificates=True\n",
        "    )\n",
        "\n",
        "    client.admin.command('ping')\n",
        "    db = client[db_name]\n",
        "    collection = db[collection_name]\n",
        "\n",
        "    print(f\"Conexión TLS establecida con éxito a {db_name}.{collection_name}\\n\")\n",
        "\n",
        "except ConnectionFailure as e:\n",
        "    print(\"No se pudo conectar con MongoDB Atlas.\")\n",
        "    print(\"Error:\", e)\n",
        "    raise SystemExit(\"No se pudo establecer la conexión. Verifica la red o la configuración TLS.\")\n",
        "\n",
        "except Exception as e:\n",
        "    print(\"Error inesperado al conectar con MongoDB:\")\n",
        "    print(e)\n",
        "    raise SystemExit(\"No se pudo establecer la conexión. Revisa tu URI o red.\")\n",
        "\n",
        "\n",
        "# Procesamiento de archivos JSON\n",
        "json_files = [f for f in os.listdir(json_input_dir) if f.endswith('.json')]\n",
        "loaded_count = 0\n",
        "failed_files = []\n",
        "\n",
        "print(f\"Iniciando carga de {len(json_files)} archivos JSON...\\n\")\n",
        "\n",
        "for i, json_file in enumerate(json_files, start=1):\n",
        "    json_path = os.path.join(json_input_dir, json_file)\n",
        "    print(f\"[{i}/{len(json_files)}] Cargando {json_file}...\")\n",
        "\n",
        "    try:\n",
        "        with open(json_path, 'r', encoding='utf-8') as f:\n",
        "            data = json.load(f)\n",
        "\n",
        "        if not data:\n",
        "            print(f\"{json_file} está vacío, se omite.\")\n",
        "            failed_files.append(json_file)\n",
        "            continue\n",
        "\n",
        "        insert_result = collection.insert_one(data)\n",
        "\n",
        "        if insert_result.inserted_id:\n",
        "            print(f\"Insertado correctamente: {json_file}\")\n",
        "            loaded_count += 1\n",
        "        else:\n",
        "            print(f\"No se devolvió ID para {json_file}\")\n",
        "            failed_files.append(json_file)\n",
        "\n",
        "    except (FileNotFoundError, json.JSONDecodeError) as e:\n",
        "        print(f\"Error de archivo en {json_file}: {e}\")\n",
        "        failed_files.append(json_file)\n",
        "\n",
        "    except PyMongoError as e:\n",
        "        print(f\"Error de MongoDB al insertar {json_file}: {e}\")\n",
        "        failed_files.append(json_file)\n",
        "\n",
        "    except Exception as e:\n",
        "        print(f\"Error inesperado en {json_file}: {str(e)}\\n{traceback.format_exc()}\")\n",
        "        failed_files.append(json_file)\n",
        "\n",
        "print(\"\\nCarga finalizada.\")\n",
        "print(f\"Archivos cargados con éxito: {loaded_count}\")\n",
        "if failed_files:\n",
        "    print(f\"Archivos con error ({len(failed_files)}): {failed_files}\")\n",
        "else:\n",
        "    print(\"Todos los archivos se cargaron correctamente.\")\n"
      ],
      "metadata": {
        "id": "zkMggPG911X9"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}