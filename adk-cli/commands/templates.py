import textwrap

AGENT_PY = textwrap.dedent("""
    from google.adk.agents import Agent
    
    def get_weather(city: str) -> dict:
        """Retrieves the current weather report for a specified city."""
        if city.lower() == "new york":
            return {"status": "success", "report": "The weather in New York is sunny with a temperature of 25 degrees Celsius (77 degrees Fahrenheit)."}
        else:
            return {"status": "error", "error_message": f"Weather information for '{city}' is not available."}
    
    def get_current_time(city: str) -> dict:
        """Returns the current time in a specified city."""
        import datetime
        from zoneinfo import ZoneInfo
        if city.lower() == "new york":
            tz_identifier = "America/New_York"
        else:
            return {"status": "error", "error_message": f"Sorry, I don't have timezone information for {city}."}
        tz = ZoneInfo(tz_identifier)
        now = datetime.datetime.now(tz)
        return {"status": "success", "report": f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"}
    
    root_agent = Agent(
        name="weather_time_agent",
        model="gemini-2.0-flash",
        description="Agent to answer questions about the time and weather in a city.",
        instruction="I can answer your questions about the time and weather in a city.",
        tools=[get_weather, get_current_time]
    )
""")

RUNNER_PY = textwrap.dedent("""
    from adk.runtime import run
    
    if __name__ == "__main__":
        run("agent:root_agent")
""")

INIT_PY = textwrap.dedent("""
    from . import agent
""")

ENV_EXAMPLE = textwrap.dedent("""
    # If using Gemini via Vertex AI on Google Cloud
    GOOGLE_CLOUD_PROJECT="your-project-id"
    GOOGLE_CLOUD_LOCATION="your-location" # e.g. us-central1
    GOOGLE_GENAI_USE_VERTEXAI="True"
""")

STREAMLIT_APP_PY = textwrap.dedent("""
    import streamlit as st
    from agent import root_agent

    st.title('Google ADK Agent Chat')
    if 'agent' not in st.session_state:
        st.session_state.agent = root_agent

    user_input = st.text_input('You:')
    if user_input:
        response = st.session_state.agent.on_message(user_input, context=None)
        st.write('Agent:', response)
""")

TEST_AGENT_PY = textwrap.dedent("""
    from agent import root_agent

    def test_respond():
        result = root_agent.on_message('hello', context=None)
        assert 'hello' in result
""")

DOCKERFILE = textwrap.dedent("""
    FROM python:3.11-slim
    WORKDIR /app
    COPY . .
    RUN pip install --no-cache-dir uv
    RUN uv pip install --system
    CMD ["python", "runner.py"]
""")

CLOUDRUN_YAML = textwrap.dedent("""
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      name: adk-agent
    spec:
      template:
        spec:
          containers:
            - image: gcr.io/PROJECT_ID/IMAGE_NAME
""")

GITIGNORE = textwrap.dedent("""
    __pycache__/
    .env
    .venv
""")

README_MD = textwrap.dedent("""
    # {project_name}

    Generated with adk-cli.

    ## Setup

    1. Install dependencies:
       ```
       uv pip install --system
       ```
    2. Run the agent CLI:
       ```
       python runner.py
       ```
    3. (Optional) Run the Streamlit app:
       ```
       streamlit run streamlit_app/app.py
       ```

    ## Deploy to Cloud Run

    See deploy/ for Dockerfile and cloudrun.yaml.
""")

PYPROJECT_TOML = textwrap.dedent("""
    [project]
    name = "adk-agent"
    version = "0.1.0"
    dependencies = [
        "google-adk",
        "streamlit",
        "pytest",
    ]
""") 