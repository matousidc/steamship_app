"""A Steamship package for prompt-based text generation.

This package provides a simple template for building a prompt-based API service.

To run:

1. Run `pip install steamship termcolor`
2. Run `ship login`
3. Run `python api.py`

To deploy and get a public API and web demo:

1. Run `echo steamship >> requirements.txt`
2. Run `echo termcolor >> requirements.txt`
3. Run `ship deploy`

To learn more about advanced uses of Steamship, read our docs at: https://docs.steamship.com/packages/using.html.
"""
from steamship.invocable import post, PackageService


class PromptPackage(PackageService):
    """Defining api endpoints"""

    # Modify this to customize behavior to match your needs.
    PROMPT = "Say an unusual greeting to {name}. Compliment them on their {trait}."

    # When this package is deployed, this annotation tells Steamship
    # to expose an endpoint that accepts HTTP POST requests for the
    # `/generate` request path.
    # See README.md for more information about deployment.
    @post("generate")
    def generate(self, name: str, trait: str) -> str:
        """Generate text from prompt parameters."""
        llm_config = {
            # Controls length of generated output.
            "max_words": 30,
            # Controls randomness of output (range: 0.0-1.0).
            "temperature": 0.8,
        }
        prompt_args = {"name": name, "trait": trait}

        llm = self.client.use_plugin("gpt-3", config=llm_config)
        return llm.generate(self.PROMPT, prompt_args)

    @post("generate_ericsson")
    def generate_ericsson(self, _prompt: str) -> str:
        """Generate text from prompt parameters."""
        llm_config = {
            # Controls length of generated output.
            "max_words": 100,
            # Controls randomness of output (range: 0.0-1.0).
            "temperature": 0.9,
        }

        prompt = "Complaint: '{_prompt}'. You are a wise old man and your job is to motivate user about their complaint, writen in quotes, according their work that is called 'Ericsson load'."
        prompt_args = {"_prompt": _prompt}
        llm = self.client.use_plugin("gpt-3", config=llm_config)
        return llm.generate(prompt, prompt_args)
