from modules.expansion import AIImageGeneratorExpansion

expansion = AIImageGeneratorExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
