
import asyncio
import os
import sys
from dotenv import load_dotenv
from core.romance_dialogo import RomanceDialogo

async def test():
    load_dotenv()
    print("PYTHON_VERSION:", sys.version)
    print("CWD:", os.getcwd())
    try:
        dialogo = RomanceDialogo()
        print("Dialogo instantiated.")
        res = await dialogo.conversar("Test message", "test-session")
        print("RESPONSE_TEXT:", res[0][:50] if res else "None")
    except Exception as e:
        print(f"EXCEPTION_TYPE: {type(e).__name__}")
        print(f"EXCEPTION_MSG: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())
