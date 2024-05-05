import requests
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy import BigInteger

Base = declarative_base()

db_url = "postgresql://postgres:machal123@database-new.chcw6o82icob.us-east-2.rds.amazonaws.com:5432/database-new"
engine = create_engine(db_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Define the database tables
class FinancialRatio(Base):
    __tablename__ = 'finmodeling_financial_ratios_new'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String)
    date = Column(DateTime)
    calendarYear = Column(String)
    period = Column(String)
    currentRatio = Column(String)
    quickRatio = Column(String)
    cashRatio = Column(String)
    daysOfSalesOutstanding = Column(String)
    daysOfInventoryOutstanding = Column(String)
    operatingCycle = Column(String)
    daysOfPayablesOutstanding = Column(String)
    cashConversionCycle = Column(String)
    grossProfitMargin = Column(String)
    operatingProfitMargin = Column(String)
    pretaxProfitMargin = Column(String)
    netProfitMargin = Column(String)
    effectiveTaxRate = Column(String)
    returnOnAssets = Column(String)
    returnOnEquity = Column(String)
    returnOnCapitalEmployed = Column(String)
    netIncomePerEBT = Column(String)
    ebtPerEbit = Column(String)
    ebitPerRevenue = Column(String)
    debtRatio = Column(String)
    debtEquityRatio = Column(String)
    longTermDebtToCapitalization = Column(String)
    totalDebtToCapitalization = Column(String)
    interestCoverage = Column(String)
    cashFlowToDebtRatio = Column(String)
    companyEquityMultiplier = Column(String)
    receivablesTurnover = Column(String)
    payablesTurnover = Column(String)
    inventoryTurnover = Column(String)
    fixedAssetTurnover = Column(String)
    assetTurnover = Column(String)
    operatingCashFlowPerShare = Column(String)
    freeCashFlowPerShare = Column(String)
    cashPerShare = Column(String)
    payoutRatio = Column(String)
    operatingCashFlowSalesRatio = Column(String)
    freeCashFlowOperatingCashFlowRatio = Column(String)
    cashFlowCoverageRatios = Column(String)
    shortTermCoverageRatios = Column(String)
    capitalExpenditureCoverageRatio = Column(String)
    dividendPaidAndCapexCoverageRatio = Column(String)
    dividendPayoutRatio = Column(String)
    priceBookValueRatio = Column(String)
    priceToBookRatio = Column(String)
    priceToSalesRatio = Column(String)
    priceEarningsRatio = Column(String)
    priceToFreeCashFlowsRatio = Column(String)
    priceToOperatingCashFlowsRatio = Column(String)
    priceCashFlowRatio = Column(String)
    priceEarningsToGrowthRatio = Column(String)
    priceSalesRatio = Column(String)
    dividendYield = Column(String)
    enterpriseValueMultiple = Column(String)
    priceFairValue = Column(String)

engine = create_engine("postgresql://postgres:machal123@database-new.chcw6o82icob.us-east-2.rds.amazonaws.com:5432/database-new")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

api_key = '577215b285ad0d4157a42a38d94d98ae'
symbols = ['AAPL', 'GS', 'GOOG', 'IBM', 'PRAA','PAAS','MSFT', 'NVDA','AMZN', 'META']  # Add more symbols if needed
limit = 500

for symbol in symbols:
    # Financial Ratios - Quarterly
    financial_ratios_url = f'https://financialmodelingprep.com/api/v3/ratios/{symbol}?period=quarter&limit={limit}&apikey={api_key}'
    financial_ratios_data = requests.get(financial_ratios_url).json()

    for data in financial_ratios_data:
        print("Data to be inserted:")
        print(data)

        # Check for potential integer out of range issues
        for key, value in data.items():
            if isinstance(value, int) and (value < -2**31 or value > 2**31 - 1):
                print(f"Potential issue with key: {key}, value: {value}")

        financial_ratio = FinancialRatio(
            symbol=str(data.get('symbol')) if data.get('symbol') is not None else None,
            date=pd.to_datetime(data.get('date')) if data.get('date') is not None else None,
            calendarYear=str(data.get('calendarYear')) if data.get('calendarYear') is not None else None,
            period=str(data.get('period')) if data.get('period') is not None else None,
            currentRatio=str(data.get('currentRatio')) if data.get('currentRatio') is not None else None,
            quickRatio=str(data.get('quickRatio')) if data.get('quickRatio') is not None else None,
            cashRatio=str(data.get('cashRatio')) if data.get('cashRatio') is not None else None,
            daysOfSalesOutstanding=str(data.get('daysOfSalesOutstanding')) if data.get('daysOfSalesOutstanding') is not None else None,
            daysOfInventoryOutstanding=str(data.get('daysOfInventoryOutstanding')) if data.get('daysOfInventoryOutstanding') is not None else None,
            operatingCycle=str(data.get('operatingCycle')) if data.get('operatingCycle') is not None else None,
            daysOfPayablesOutstanding=str(data.get('daysOfPayablesOutstanding')) if data.get('daysOfPayablesOutstanding') is not None else None,
            cashConversionCycle=str(data.get('cashConversionCycle')) if data.get('cashConversionCycle') is not None else None,
            grossProfitMargin=str(data.get('grossProfitMargin')) if data.get('grossProfitMargin') is not None else None,
            operatingProfitMargin=str(data.get('operatingProfitMargin')) if data.get('operatingProfitMargin') is not None else None,
            pretaxProfitMargin=str(data.get('pretaxProfitMargin')) if data.get('pretaxProfitMargin') is not None else None,
            netProfitMargin=str(data.get('netProfitMargin')) if data.get('netProfitMargin') is not None else None,
            effectiveTaxRate=str(data.get('effectiveTaxRate')) if data.get('effectiveTaxRate') is not None else None,
            returnOnAssets=str(data.get('returnOnAssets')) if data.get('returnOnAssets') is not None else None,
            returnOnEquity=str(data.get('returnOnEquity')) if data.get('returnOnEquity') is not None else None,
            returnOnCapitalEmployed=str(data.get('returnOnCapitalEmployed')) if data.get('returnOnCapitalEmployed') is not None else None,
            netIncomePerEBT=str(data.get('netIncomePerEBT')) if data.get('netIncomePerEBT') is not None else None,
            ebtPerEbit=str(data.get('ebtPerEbit')) if data.get('ebtPerEbit') is not None else None,
            ebitPerRevenue=str(data.get('ebitPerRevenue')) if data.get('ebitPerRevenue') is not None else None,
            debtRatio=str(data.get('debtRatio')) if data.get('debtRatio') is not None else None,
            debtEquityRatio=str(data.get('debtEquityRatio')) if data.get('debtEquityRatio') is not None else None,
            longTermDebtToCapitalization=str(data.get('longTermDebtToCapitalization')) if data.get('longTermDebtToCapitalization') is not None else None,
            totalDebtToCapitalization=str(data.get('totalDebtToCapitalization')) if data.get('totalDebtToCapitalization') is not None else None,
            interestCoverage=str(data.get('interestCoverage')) if data.get('interestCoverage') is not None else None,
            cashFlowToDebtRatio=str(data.get('cashFlowToDebtRatio')) if data.get('cashFlowToDebtRatio') is not None else None,
            companyEquityMultiplier=str(data.get('companyEquityMultiplier')) if data.get('companyEquityMultiplier') is not None else None,
            receivablesTurnover=str(data.get('receivablesTurnover')) if data.get('receivablesTurnover') is not None else None,
            payablesTurnover=str(data.get('payablesTurnover')) if data.get('payablesTurnover') is not None else None,
            inventoryTurnover=str(data.get('inventoryTurnover')) if data.get('inventoryTurnover') is not None else None,
            fixedAssetTurnover=str(data.get('fixedAssetTurnover')) if data.get('fixedAssetTurnover') is not None else None,
            assetTurnover=str(data.get('assetTurnover')) if data.get('assetTurnover') is not None else None,
            operatingCashFlowPerShare=str(data.get('operatingCashFlowPerShare')) if data.get('operatingCashFlowPerShare') is not None else None,
            freeCashFlowPerShare=str(data.get('freeCashFlowPerShare')) if data.get('freeCashFlowPerShare') is not None else None,
            cashPerShare=str(data.get('cashPerShare')) if data.get('cashPerShare') is not None else None,
            payoutRatio=str(data.get('payoutRatio')) if data.get('payoutRatio') is not None else None,
            operatingCashFlowSalesRatio=str(data.get('operatingCashFlowSalesRatio')) if data.get('operatingCashFlowSalesRatio') is not None else None,
            freeCashFlowOperatingCashFlowRatio=str(data.get('freeCashFlowOperatingCashFlowRatio')) if data.get('freeCashFlowOperatingCashFlowRatio') is not None else None,
            cashFlowCoverageRatios=str(data.get('cashFlowCoverageRatios')) if data.get('cashFlowCoverageRatios') is not None else None,
            shortTermCoverageRatios=str(data.get('shortTermCoverageRatios')) if data.get('shortTermCoverageRatios') is not None else None,
            capitalExpenditureCoverageRatio=str(data.get('capitalExpenditureCoverageRatio')) if data.get('capitalExpenditureCoverageRatio') is not None else None,
            dividendPaidAndCapexCoverageRatio=str(data.get('dividendPaidAndCapexCoverageRatio')) if data.get('dividendPaidAndCapexCoverageRatio') is not None else None,
            dividendPayoutRatio=str(data.get('dividendPayoutRatio')) if data.get('dividendPayoutRatio') is not None else None,
            priceBookValueRatio=str(data.get('priceBookValueRatio')) if data.get('priceBookValueRatio') is not None else None,
            priceToBookRatio=str(data.get('priceToBookRatio')) if data.get('priceToBookRatio') is not None else None,
            priceToSalesRatio=str(data.get('priceToSalesRatio')) if data.get('priceToSalesRatio') is not None else None,
            priceEarningsRatio=str(data.get('priceEarningsRatio')) if data.get('priceEarningsRatio') is not None else None,
            priceToFreeCashFlowsRatio=str(data.get('priceToFreeCashFlowsRatio')) if data.get('priceToFreeCashFlowsRatio') is not None else None,
            priceToOperatingCashFlowsRatio=str(data.get('priceToOperatingCashFlowsRatio')) if data.get('priceToOperatingCashFlowsRatio') is not None else None,
            priceCashFlowRatio=str(data.get('priceCashFlowRatio')) if data.get('priceCashFlowRatio') is not None else None,
            priceEarningsToGrowthRatio=str(data.get('priceEarningsToGrowthRatio')) if data.get('priceEarningsToGrowthRatio') is not None else None,
            priceSalesRatio=str(data.get('priceSalesRatio')) if data.get('priceSalesRatio') is not None else None,
            dividendYield=str(data.get('dividendYield')) if data.get('dividendYield') is not None else None,
            enterpriseValueMultiple=str(data.get('enterpriseValueMultiple')) if data.get('enterpriseValueMultiple') is not None else None,
            priceFairValue=str(data.get('priceFairValue')) if data.get('priceFairValue') is not None else None
        )

        session.add(financial_ratio)

    session.commit()

session.close()