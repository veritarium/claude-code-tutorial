# Chapter 6: MCP Servers

## What is MCP?

Model Context Protocol (MCP) is an open protocol that allows Claude Code to connect to external tools and data sources. MCP servers extend Claude's capabilities beyond its built-in tools, enabling integration with databases, APIs, custom tooling, and more.

## How MCP Works

```
┌─────────────┐     MCP Protocol     ┌─────────────┐
│ Claude Code │ ◄──────────────────► │ MCP Server  │
└─────────────┘                      └─────────────┘
                                            │
                                            ▼
                                     ┌─────────────┐
                                     │  Resources  │
                                     │  (DB, API,  │
                                     │   Files)    │
                                     └─────────────┘
```

Claude Code acts as an MCP client, connecting to one or more MCP servers. Each server exposes:
- **Tools**: Actions Claude can perform (query database, send email, etc.)
- **Resources**: Data Claude can read (files, database records, etc.)
- **Prompts**: Pre-defined prompt templates

## Built-in vs Custom MCP Servers

### Community MCP Servers

Popular pre-built servers available:

- **Filesystem**: Extended file operations
- **PostgreSQL/MySQL**: Direct database access
- **GitHub**: Repository management beyond git
- **Slack**: Read and send messages
- **Google Drive**: Access cloud documents
- **Puppeteer**: Browser automation

### Custom MCP Servers

You can build your own servers for:
- Internal APIs and services
- Proprietary databases
- Custom business logic
- Legacy system integration

## Configuring MCP Servers

### Configuration File Location

MCP servers are configured in your Claude Code settings:

```
~/.claude/settings.json
```

Or project-specific:

```
.claude/settings.json
```

### Basic Configuration

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    }
  }
}
```

### Configuration Fields

| Field | Description |
|-------|-------------|
| `command` | The executable to run |
| `args` | Command-line arguments |
| `env` | Environment variables |
| `cwd` | Working directory |

## Common MCP Server Setups

### PostgreSQL Database

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://user:pass@localhost:5432/mydb"
      }
    }
  }
}
```

**Usage with Claude:**
```
Query the users table for all active accounts created this month
```

```
Show me the schema for the orders table
```

### GitHub Integration

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**Usage with Claude:**
```
List all open issues labeled "bug" in my repo
```

```
Create an issue for the authentication bug we just found
```

### Slack Integration

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token"
      }
    }
  }
}
```

**Usage with Claude:**
```
Read the last 10 messages from #engineering
```

```
Post a deployment notification to #releases
```

### Puppeteer (Browser Automation)

```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

**Usage with Claude:**
```
Open the staging site and take a screenshot of the login page
```

```
Fill out the contact form with test data and submit it
```

## Multiple MCP Servers

You can configure multiple servers simultaneously:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://localhost/mydb"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_token"
      }
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-token"
      }
    }
  }
}
```

Claude automatically discovers and uses tools from all connected servers.

## Building a Custom MCP Server

### When to Build Custom

Build your own MCP server when you need to:
- Connect to internal/proprietary systems
- Implement custom business logic
- Create specialized tools for your workflow
- Integrate with systems without existing servers

### Basic Server Structure (TypeScript)

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  { name: "my-custom-server", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// Define a tool
server.setRequestHandler("tools/list", async () => ({
  tools: [
    {
      name: "get_customer",
      description: "Fetch customer details by ID",
      inputSchema: {
        type: "object",
        properties: {
          customer_id: { type: "string", description: "The customer ID" }
        },
        required: ["customer_id"]
      }
    }
  ]
}));

// Handle tool calls
server.setRequestHandler("tools/call", async (request) => {
  if (request.params.name === "get_customer") {
    const { customer_id } = request.params.arguments;
    // Your logic here
    const customer = await fetchCustomer(customer_id);
    return { content: [{ type: "text", text: JSON.stringify(customer) }] };
  }
});

// Start the server
const transport = new StdioServerTransport();
await server.connect(transport);
```

### Installing Your Custom Server

```json
{
  "mcpServers": {
    "my-custom": {
      "command": "node",
      "args": ["/path/to/my-server/index.js"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

## Security Considerations

### Principle of Least Privilege

Only grant servers access to what they need:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/specific/project/path"
      ]
    }
  }
}
```

### Sensitive Data

Never hardcode secrets in config files. Use environment variables:

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${DB_CONNECTION_STRING}"
      }
    }
  }
}
```

### Review Server Permissions

Before enabling an MCP server:
1. Understand what actions it can perform
2. Verify the source is trusted
3. Limit scope where possible
4. Monitor usage in sensitive environments

## Troubleshooting

### Server Not Connecting

Check that the command works standalone:
```bash
npx -y @modelcontextprotocol/server-postgres
```

### Missing Tools

Verify the server is listed:
```
What MCP servers are connected?
```

### Permission Errors

Ensure environment variables are set correctly and credentials are valid.

### Debug Mode

Run Claude Code with verbose logging to diagnose MCP issues:
```bash
claude --debug
```

## Practical Workflows with MCP

### Database-Driven Development

With PostgreSQL MCP:

```
Show me the current schema for the users table
```

```
Write a migration to add an email_verified column
```

```
Query for users who signed up in the last week but haven't verified their email
```

### Automated Issue Management

With GitHub MCP:

```
Find all issues assigned to me that are overdue
```

```
Close issue #42 with a comment explaining the fix in commit abc123
```

```
Create issues for each TODO comment in the codebase
```

### Cross-System Workflows

With multiple servers:

```
Query the database for failed orders, then create a GitHub issue for each one and post a summary to #engineering on Slack
```

## Exercise: Setting Up MCP

1. **Install a community server:**

   Add the filesystem server to your config and verify it works:
   ```
   List files in the allowed directory using the MCP filesystem server
   ```

2. **Configure database access:**

   Set up the PostgreSQL server and run a query:
   ```
   Show me all tables in the database
   ```

3. **Create a workflow:**

   Combine multiple MCP servers:
   ```
   Query the database for recent errors, create a GitHub issue summarizing them, and notify the team on Slack
   ```

## Summary

MCP servers extend Claude Code's capabilities:

- **Connect** to databases, APIs, and external services
- **Configure** servers through JSON settings files
- **Combine** multiple servers for powerful workflows
- **Build** custom servers for proprietary systems

Key principles:
- Start with community servers for common integrations
- Use project-specific configs for project-specific tools
- Follow security best practices with credentials
- Build custom servers only when needed

---

[← Previous: Advanced Workflows](05-advanced-workflows.md) | [Home](../README.md)
