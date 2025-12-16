from transformers import AutoTokenizer, AutoModelForCausalLM


class modelQuerry:
    def __init__(self, document, querry):
        self.document = document
        self.querry = querry
        self.tokenizer = AutoTokenizer.from_pretrained(
            'TinyLlama/TinyLlama-1.1B-Chat-v1.0')

        self.model = AutoModelForCausalLM.from_pretrained(
            "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            torch_dtype="auto",
            device_map="auto"
        )

    def build_prompt(self):
        context = self.document
        prompt = f"""
        You are a helpful assistant.
        Answer the question using ONLY the context below.
        If the answer is not in the context, say "I don't know".

        Context:
        {context}

        Question:
        {self.querry}

        Answer:
        """
        return prompt

    def generate_answer(self):
        prompt = self.build_prompt()

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=300
        )

        decoded_text = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        if "Answer:" in decoded_text:
            answer = decoded_text.split("Answer:")[-1].strip()
        else:
            answer = decoded_text.strip()



        return answer
