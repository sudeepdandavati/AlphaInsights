import { useState } from "react";

import "../styles/Comparison.css";

import { compareDocuments } from "../services/api";

import ComparisonSelector from "./ComparisonSelector";
import ComparisonTable from "./ComparisonTable";
import FinancialCharts from "./FinancialCharts";

function ComparisonWorkspace({ documents }) {

    const [selectedDocuments, setSelectedDocuments] = useState([]);

    const [comparisonData, setComparisonData] = useState(null);

    const [loading, setLoading] = useState(false);

    const handleCompare = async () => {

        if (selectedDocuments.length < 2) {
            return;
        }

        setLoading(true);

        try {

            const response = await compareDocuments(

                selectedDocuments.map(
                    (document) => document.id
                )

            );

            setComparisonData(response);

        } catch (error) {

            console.error(
                "Comparison failed:",
                error
            );

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="comparison-workspace">

            <ComparisonSelector
                documents={documents}
                selectedDocuments={selectedDocuments}
                setSelectedDocuments={setSelectedDocuments}
                onCompare={handleCompare}
            />

            {loading && (

                <p className="comparison-loading">
                    Comparing selected reports...
                </p>

            )}

            {!loading && comparisonData && (

                <>

                    <ComparisonTable
                        comparisonData={comparisonData}
                    />

                    <FinancialCharts
                        comparisonData={comparisonData}
                    />

                    <div className="comparison-summary">

                        <h2 className="comparison-title">
                            🤖 AI Financial Summary
                        </h2>

                        <div className="summary-card">

                            <p className="summary-text">
                                {comparisonData.summary}
                            </p>

                        </div>

                    </div>

                </>

            )}

        </div>

    );

}

export default ComparisonWorkspace;