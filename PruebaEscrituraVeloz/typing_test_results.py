class TypingTestResults:
    def __init__(self):
        self.reset()

    def reset(self):
        self.results_by_sentence = {} # Diccionario para rastrear resultados por frase
        
    def set_correct_sentence(self, sentence):
        sentence = sentence.lower()
        self.results_by_sentence[sentence] = {'times': [], 'accuracies': []}

    def calculate_accuracy(self, user_input, correct_sentence):
        # Calcula la precisión utilizando self.correct_sentence
        correct_chars = sum(c1 == c2 for c1, c2 in zip(user_input, correct_sentence))
        if len(correct_sentence) == 0:
            return 100.0  # Tratar una oración vacía como 100% de precisión
        accuracy = (correct_chars / len(correct_sentence)) * 100
        return accuracy
    
    def add_result(self, elapsed_time, accuracy, sentence):
        sentence = sentence.lower()
        sentence_results = self.results_by_sentence.get(sentence, {'times': [], 'accuracies': []})
        sentence_results['times'].append(elapsed_time)
        sentence_results['accuracies'].append(accuracy)
        self.results_by_sentence[sentence] = sentence_results
        
    def get_last_result(self):
        if self.results_by_sentence:
            sentence = list(self.results_by_sentence.keys())[-1]
            results = self.results_by_sentence[sentence]
            elapsed_time = results['times'][-1]
            accuracy = results['accuracies'][-1]
            return f"Último resultado para '{sentence}': Tiempo: {elapsed_time:.2f} segundos | Precisión: {accuracy:.2f}%"
        else:
            return "No hay resultados disponibles."




    def __str__(self):
        result_str = "\n".join([f"Tiempo: {time:.2f} segundos | Precisión: {acc:.2f}%" for time, acc in self.results_by_sentence.items()])
        return result_str

