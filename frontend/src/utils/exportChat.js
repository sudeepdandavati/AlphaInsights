export function exportAsMarkdown(messages, documentInfo) {

    if (!messages || messages.length === 0) {
        return;
    }

    let markdown = "# AlphaInsights Conversation\n\n";

    if (documentInfo) {

        markdown += "## Document\n\n";
        markdown += `${documentInfo.document.name}\n\n`;

        markdown += `- Pages: ${documentInfo.pages}\n`;
        markdown += `- Chunks: ${documentInfo.chunks}\n`;
        markdown += `- Embeddings: ${documentInfo.embeddings}\n\n`;
    }

    markdown += "---\n\n";

    messages.forEach((message, index) => {

        markdown += `# Question ${index + 1}\n\n`;

        markdown += `**Question**\n\n`;
        markdown += `${message.question}\n\n`;

        markdown += `**Answer**\n\n`;
        markdown += `${message.answer}\n\n`;

        if (message.sources && message.sources.length > 0) {

            markdown += `**Sources**\n\n`;

            message.sources.forEach((source) => {

                markdown += `- Chunk ${source.chunk_id} (${(
                    source.score * 100
                ).toFixed(1)}% Match)\n`;

            });

            markdown += "\n";

        }

        markdown += "---\n\n";

    });

    const blob = new Blob(
        [markdown],
        {
            type: "text/markdown;charset=utf-8",
        }
    );

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.download = "AlphaInsights_Conversation.md";

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    URL.revokeObjectURL(url);

}