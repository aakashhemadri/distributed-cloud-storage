COUNT=`python<<EOF
import json
json_data = open('config.json')
data = json.load(json_data)
json_data.close()
print(data['node_count'])
EOF `
echo $COUNT
for (( i=1; i<=$COUNT; i++ ))
do
    ./start_flask.sh $i &
done
