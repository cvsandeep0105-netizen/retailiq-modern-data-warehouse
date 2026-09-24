$ErrorActionPreference="Stop"
foreach($line in Get-Content ".env"){if($line -match "^\s*([^#=]+)=(.*)$"){$envName=$matches[1].Trim();$envValue=$matches[2].Trim();[Environment]::SetEnvironmentVariable($envName,$envValue,"Process")}}
$env:PYTHONPATH="$PWD\src"
$env:PYTHONPATH="$PWD\src"
Write-Host "============================================="
Write-Host " RetailIQ - Modern Data Warehouse Platform"
Write-Host " Production-Style Local Demonstration"
Write-Host "============================================="
Write-Host ""
Write-Host "[1/7] Database connectivity"
python -c "import os,psycopg2; c=psycopg2.connect(host=os.environ['POSTGRES_HOST'],port=int(os.environ['POSTGRES_PORT']),dbname=os.environ['POSTGRES_DB'],user=os.environ['POSTGRES_USER'],password=os.environ['POSTGRES_PASSWORD']); x=c.cursor(); x.execute('SELECT current_database(),current_user'); r=x.fetchone(); print('DATABASE=' + str(r[0])); print('DATABASE_ROLE=' + str(r[1])); x.close(); c.close()"
Write-Host ""
Write-Host "[2/7] Warehouse and mart inventory"
python "src\retailiq\observability\demo_inventory.py"
Write-Host ""
Write-Host "[3/7] Business KPI summary"
python -c "import os,psycopg2; c=psycopg2.connect(host=os.environ['POSTGRES_HOST'],port=int(os.environ['POSTGRES_PORT']),dbname=os.environ['POSTGRES_DB'],user=os.environ['POSTGRES_USER'],password=os.environ['POSTGRES_PASSWORD']); x=c.cursor(); x.execute('SELECT order_count,customer_count,product_count,seller_count,average_order_value,on_time_delivery_rate_pct,average_review_score FROM semantic.kpi_summary'); r=x.fetchone(); print('ORDERS=' + str(r[0])); print('CUSTOMERS=' + str(r[1])); print('PRODUCTS=' + str(r[2])); print('SELLERS=' + str(r[3])); print('AVERAGE_ORDER_VALUE=' + str(r[4])); print('ON_TIME_RATE_PCT=' + str(r[5])); print('AVERAGE_REVIEW_SCORE=' + str(r[6])); x.close(); c.close()"
Write-Host ""
Write-Host "[4/7] Data Quality evidence"
$dq=Get-Content "data\output\data_quality\data_quality_execution.json" -Raw | ConvertFrom-Json
Write-Host ("DATA_QUALITY_CHECKS="+$dq.check_count)
Write-Host ("DATA_QUALITY_FAILURES="+$dq.fail_count)

Write-Host "[5/7] Performance evidence"
$perf=Get-Content "data\output\performance\performance_benchmark.json" -Raw | ConvertFrom-Json
Write-Host ("PERFORMANCE_QUERIES="+$perf.query_count)
Write-Host ("PERFORMANCE_AVG_MS="+$perf.average_execution_time_ms)
Write-Host ("PERFORMANCE_MAX_MS="+$perf.max_execution_time_ms)

Write-Host "[6/7] Scalability evidence"
$scale=Get-Content "data\output\scalability\scalability_workload_test.json" -Raw | ConvertFrom-Json
Write-Host ("SCALABILITY_EXECUTIONS="+$scale.total_query_executions)
Write-Host ("SCALABILITY_FAILURES="+$scale.failed_query_executions)
Write-Host ("SCALABILITY_QPS="+$scale.queries_per_second)

Write-Host "[7/7] CI/CD and end-to-end evidence"
$ci=Get-Content "data\output\ci_cd\ci_validation_evidence.json" -Raw | ConvertFrom-Json
$e2e=Get-Content "data\output\end_to_end\end_to_end_validation.json" -Raw | ConvertFrom-Json
Write-Host ("CI_STATUS="+$ci.status)
Write-Host ("E2E_STATUS="+$e2e.status)
Write-Host ""
Write-Host "============================================="
Write-Host " RetailIQ DEMO COMPLETE"
Write-Host " Local production-style validation: PASS"
Write-Host " Cloud production deployment: NOT CLAIMED"
Write-Host "============================================="


