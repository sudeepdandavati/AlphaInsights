import { useEffect, useState } from "react";

import "../styles/FinancialDashboard.css";

import { getFinancialMetrics } from "../services/api";

function FinancialDashboard({ selectedDocument }) {

    const [metrics, setMetrics] = useState(null);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        if (!selectedDocument) {

            setMetrics(null);

            return;

        }

        const loadMetrics = async () => {

            setLoading(true);

            try {

                const data = await getFinancialMetrics(
                    selectedDocument.id
                );

                setMetrics(data);

            } catch (error) {

                console.error(
                    "Failed to load financial metrics:",
                    error
                );

                setMetrics(null);

            } finally {

                setLoading(false);

            }

        };

        loadMetrics();

    }, [selectedDocument]);

    if (!selectedDocument) {

        return null;

    }

    return (

        <div className="financial-dashboard">

            <h2 className="financial-title">
                📊 Financial Overview
            </h2>

            {loading ? (

                <p className="financial-loading">
                    Loading financial metrics...
                </p>

            ) : (

                <div className="financial-grid">

                    <div className="metric-card">
                        <span className="metric-label">Revenue</span>
                        <span className="metric-value">
                            {metrics?.revenue || "—"}
                        </span>
                    </div>

                    <div className="metric-card">
                        <span className="metric-label">Net Income</span>
                        <span className="metric-value">
                            {metrics?.net_income || "—"}
                        </span>
                    </div>

                    <div className="metric-card">
                        <span className="metric-label">Gross Profit</span>
                        <span className="metric-value">
                            {metrics?.gross_profit || "—"}
                        </span>
                    </div>

                    <div className="metric-card">
                        <span className="metric-label">Operating Income</span>
                        <span className="metric-value">
                            {metrics?.operating_income || "—"}
                        </span>
                    </div>

                    <div className="metric-card">
                        <span className="metric-label">EPS</span>
                        <span className="metric-value">
                            {metrics?.eps || "—"}
                        </span>
                    </div>

                    <div className="metric-card">
                        <span className="metric-label">Cash</span>
                        <span className="metric-value">
                            {metrics?.cash || "—"}
                        </span>
                    </div>

                    <div className="metric-card">
                        <span className="metric-label">Total Assets</span>
                        <span className="metric-value">
                            {metrics?.total_assets || "—"}
                        </span>
                    </div>

                    <div className="metric-card">
                        <span className="metric-label">Total Liabilities</span>
                        <span className="metric-value">
                            {metrics?.total_liabilities || "—"}
                        </span>
                    </div>

                    <div className="metric-card">
                        <span className="metric-label">Total Debt</span>
                        <span className="metric-value">
                            {metrics?.total_debt || "—"}
                        </span>
                    </div>

                </div>

            )}

        </div>

    );

}

export default FinancialDashboard;