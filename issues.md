# Issue 1

In the beginning I got this error:

```
pulkit@Pulkits-MacBook-Pro voice-agent-workshop-starter % python3 verify_setup.py

=== Voice Agent Workshop — Setup Verification ===

✓ Python 3.14

--- Environment variables ---
✓ LIVEKIT_URL present (37 chars)
✓ LIVEKIT_API_KEY present (15 chars)
✓ LIVEKIT_API_SECRET present (44 chars)
✓ GROQ_API_KEY present (56 chars)
✓ SMALLEST_API_KEY present (35 chars)
✓ NOVEUM_API_KEY present (35 chars)

--- Live API checks ---
✓ Groq API reachable + key valid
✗ Smallest.ai returned HTTP 404: {"message":"Cannot GET /waves/v1/lightning-v3.1/voices","path":"/api/v1/lightning-v3.1/voices","originalUrl":"/waves/v1/
✓ Noveum API reachable + key valid

--- Tooling ---
! LiveKit CLI not found. Optional but recommended: `brew install livekit-cli` (macOS) or see https://docs.livekit.io/realtime/cli/

1 check(s) failed. Fix before Thursday or join Wednesday office hours.
```

# Issue 2



# Issue 3

In the readme mention python3 not python

# Issue 4

```
(.venv) pulkit@Pulkits-MacBook-Pro voice-agent-workshop-starter % python3 agent.py dev  
    18:03:31.015 DEBUG    asyncio            Using selector: KqueueSelector  
    18:03:31.017 DEV      livekit.agents     Watching /Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter  
    18:03:31.932 DEBUG    asyncio            Using selector: KqueueSelector  
    18:03:31.937 INFO     livekit.agents     starting worker {"version": "1.5.8", "rtc-version": "1.1.7"}
                 INFO     livekit.agents     plugin registered {"plugin": "livekit.plugins.openai", "version": "1.5.8"}
                 INFO     livekit.agents     plugin registered {"plugin": "livekit.plugins.groq", "version": "1.5.8"}
    18:03:31.938 INFO     livekit.agents     plugin registered {"plugin": "livekit.plugins.silero", "version": "1.5.8"}
                 INFO     livekit.agents     plugin registered {"plugin": "livekit.plugins.smallestai", "version": "1.5.8"}
    18:03:31.940 INFO     livekit.agents     HTTP server listening on :59009  
    18:03:32.207 WARNING  livekit.agents     failed to connect to livekit, retrying in 0s  
Traceback (most recent call last):
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1325, in _wrap_create_connection
    return await self._loop.create_connection(*args, **kwargs, sock=sock)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/base_events.py", line 1198, in create_connection
    transport, protocol = await self._create_connection_transport(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
        ssl_shutdown_timeout=ssl_shutdown_timeout)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/base_events.py", line 1231, in _create_connection_transport
    await waiter
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/sslproto.py", line 581, in _on_handshake_complete
    raise handshake_exc
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/sslproto.py", line 563, in _do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/ssl.py", line 951, in do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1081)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/livekit/agents/worker.py", line 1042, in _connection_task
    ws = await self._http_session.ws_connect(
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<6 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 1087, in _ws_connect
    resp = await self.request(
           ^^^^^^^^^^^^^^^^^^^
    ...<11 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 788, in _request
    resp = await handler(req)
           ^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 742, in _connect_and_send_request
    conn = await self._connector.connect(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        req, traces=traces, timeout=real_timeout
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 672, in connect
    proto = await self._create_connection(req, traces, timeout)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1251, in _create_connection
    _, proto = await self._create_direct_connection(req, traces, timeout)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1623, in _create_direct_connection
    raise last_exc
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1592, in _create_direct_connection
    transp, proto = await self._wrap_create_connection(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<7 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1327, in _wrap_create_connection
    raise ClientConnectorCertificateError(req.connection_key, exc) from exc
aiohttp.client_exceptions.ClientConnectorCertificateError: Cannot connect to host workshop-9exr47vp.livekit.cloud:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] 
certificate verify failed: unable to get local issuer certificate (_ssl.c:1081)')]

```
18:03:32.413 WARNING  livekit.agents     failed to connect to livekit, retrying in 2s  
```

Traceback (most recent call last):
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1325, in _wrap_create_connection
    return await self._loop.create_connection(*args, **kwargs, sock=sock)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/base_events.py", line 1198, in create_connection
    transport, protocol = await self._create_connection_transport(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
        ssl_shutdown_timeout=ssl_shutdown_timeout)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/base_events.py", line 1231, in _create_connection_transport
    await waiter
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/sslproto.py", line 581, in _on_handshake_complete
    raise handshake_exc
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/sslproto.py", line 563, in _do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/ssl.py", line 951, in do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1081)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/livekit/agents/worker.py", line 1042, in _connection_task
    ws = await self._http_session.ws_connect(
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<6 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 1087, in _ws_connect
    resp = await self.request(
           ^^^^^^^^^^^^^^^^^^^
    ...<11 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 788, in _request
    resp = await handler(req)
           ^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 742, in _connect_and_send_request
    conn = await self._connector.connect(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        req, traces=traces, timeout=real_timeout
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 672, in connect
    proto = await self._create_connection(req, traces, timeout)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1251, in _create_connection
    _, proto = await self._create_direct_connection(req, traces, timeout)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1623, in _create_direct_connection
    raise last_exc
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1592, in _create_direct_connection
    transp, proto = await self._wrap_create_connection(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<7 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1327, in _wrap_create_connection
    raise ClientConnectorCertificateError(req.connection_key, exc) from exc
aiohttp.client_exceptions.ClientConnectorCertificateError: Cannot connect to host workshop-9exr47vp.livekit.cloud:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] 
certificate verify failed: unable to get local issuer certificate (_ssl.c:1081)')]

```
18:03:34.602 WARNING  livekit.agents     failed to connect to livekit, retrying in 4s  
```

Traceback (most recent call last):
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1325, in _wrap_create_connection
    return await self._loop.create_connection(*args, **kwargs, sock=sock)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/base_events.py", line 1198, in create_connection
    transport, protocol = await self._create_connection_transport(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
        ssl_shutdown_timeout=ssl_shutdown_timeout)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/base_events.py", line 1231, in _create_connection_transport
    await waiter
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/sslproto.py", line 581, in _on_handshake_complete
    raise handshake_exc
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/sslproto.py", line 563, in _do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/ssl.py", line 951, in do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1081)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/livekit/agents/worker.py", line 1042, in _connection_task
    ws = await self._http_session.ws_connect(
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<6 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 1087, in _ws_connect
    resp = await self.request(
           ^^^^^^^^^^^^^^^^^^^
    ...<11 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 788, in _request
    resp = await handler(req)
           ^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 742, in _connect_and_send_request
    conn = await self._connector.connect(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        req, traces=traces, timeout=real_timeout
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 672, in connect
    proto = await self._create_connection(req, traces, timeout)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1251, in _create_connection
    _, proto = await self._create_direct_connection(req, traces, timeout)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1623, in _create_direct_connection
    raise last_exc
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1592, in _create_direct_connection
    transp, proto = await self._wrap_create_connection(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<7 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1327, in _wrap_create_connection
    raise ClientConnectorCertificateError(req.connection_key, exc) from exc
aiohttp.client_exceptions.ClientConnectorCertificateError: Cannot connect to host workshop-9exr47vp.livekit.cloud:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] 
certificate verify failed: unable to get local issuer certificate (_ssl.c:1081)')]

```
18:03:38.778 WARNING  livekit.agents     failed to connect to livekit, retrying in 6s  
```

Traceback (most recent call last):
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1325, in _wrap_create_connection
    return await self._loop.create_connection(*args, **kwargs, sock=sock)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/base_events.py", line 1198, in create_connection
    transport, protocol = await self._create_connection_transport(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
        ssl_shutdown_timeout=ssl_shutdown_timeout)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/base_events.py", line 1231, in _create_connection_transport
    await waiter
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/sslproto.py", line 581, in _on_handshake_complete
    raise handshake_exc
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/sslproto.py", line 563, in _do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/ssl.py", line 951, in do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1081)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/livekit/agents/worker.py", line 1042, in _connection_task
    ws = await self._http_session.ws_connect(
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<6 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 1087, in _ws_connect
    resp = await self.request(
           ^^^^^^^^^^^^^^^^^^^
    ...<11 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 788, in _request
    resp = await handler(req)
           ^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/client.py", line 742, in _connect_and_send_request
    conn = await self._connector.connect(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        req, traces=traces, timeout=real_timeout
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 672, in connect
    proto = await self._create_connection(req, traces, timeout)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1251, in _create_connection
    _, proto = await self._create_direct_connection(req, traces, timeout)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1623, in _create_direct_connection
    raise last_exc
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1592, in _create_direct_connection
    transp, proto = await self._wrap_create_connection(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<7 lines>...
    )
    ^
  File "/Users/pulkit/Desktop/samaan/vid-edit/voice-agent-workshop-starter/.venv/lib/python3.14/site-packages/aiohttp/connector.py", line 1327, in _wrap_create_connection
    raise ClientConnectorCertificateError(req.connection_key, exc) from exc
aiohttp.client_exceptions.ClientConnectorCertificateError: Cannot connect to host workshop-9exr47vp.livekit.cloud:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] 
certificate verify failed: unable to get local issuer certificate (_ssl.c:1081)')]

^C    18:03:40.595 INFO     livekit.agents     shutting down worker {"id": "unregistered"}

```