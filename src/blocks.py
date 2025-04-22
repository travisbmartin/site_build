# blocks.py
from enum import Enum

BlockType = Enum('BlockType', ['paragraph', 'heading', 'code', 'quote', 'unordered_list', 'ordered_list'])
