import os
from dotenv import load_dotenv
from openai import OpenAI
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console

# Pintar todas las variables de entorno
for key, value in os.environ.items():
    print(f"[bold blue]{key}[/bold blue]: [white]{value}[/white]")


console = Console()

console.print(Panel("[bold green]🚀 Starting AI App...[/bold green]", expand=False, border_style="green"))

# Print the environment variables for debugging
llm_url = os.getenv('LLM_URL')
llm_model = os.getenv('LLM_MODEL')
console.print(f"[bold cyan]LLM_URL:[/bold cyan] [white]{llm_url}[/white]")
console.print(f"[bold cyan]LLM_MODEL:[/bold cyan] [white]{llm_model}[/white]")

# Create OpenAI client
client = OpenAI(
    base_url=llm_url,
    api_key="docker",
)

prompt = """
Dame un título de YouTube para la siguiente descripción: ¡Hola developer! En este vídeo quiero mostrarte cómo 
puedes usar Docker Compose junto con Docker Model Runner para desarrollar tus aplicaciones con IA mucho más rápido.
Gracias a que puedes descargar y levantar modelos definidos como parte de tu Docker Compose.
"""


# Call the OpenAI API to generate text
response = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}], 
    model=llm_model
)

# Pretty print the response in a panel
content = response.choices[0].message.content
console.print(Panel(f"[bold yellow]Response from OpenAI:[/bold yellow]\n[white]{content}[/white]", title="🤖 OpenAI", border_style="magenta"))