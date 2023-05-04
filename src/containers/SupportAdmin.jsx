import { Button, Table } from 'antd'
import axios from "axios";

import React, { useEffect, useState } from 'react'
import { supportAdminURL } from '../constants';

const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      render: (text) => <a>{text}</a>,
    },
    {
      title: 'Price',
      dataIndex: 'price',
      key: 'price',
    },
    
]

const SupportAdmin = () => {
    const [data1,setData1] = useState([])
    const [data2,setData2] = useState([])

    // useEffect(()=>{
    //     var config = {
    //         method: 'get',
    //         url: '/visualization/13/',
            
    //     };
    //     return axios(config).then( (res) => {
    //         setData1(res.trivela.content)
    //         setData2(res.oss.content)
    //       })
    //       .catch(function (error) {
    //         console.log(error);
    //       });
    // })

    const fetchSupportAdmin = () => {
        axios.defaults.baseURL = 'http://127.0.0.1:8000';

        var config = {
            method: 'get',
            url: '/visualization/13/',
            
        };
        return axios(config).then((res) => {
            setData1(res.data.trivela.content)
            setData2(res.data.oss.content)
            console.log(res)
          })
          .catch(function (error) {
            console.log(error);
          });
    }


    return (
        <div style={{padding: "180px", marginTop: "-153px"}}>
            <Button onClick={fetchSupportAdmin}>Xem thông tin hỗ trợ</Button>
            <Table style={{marginTop: "20px"}} columns={columns} dataSource={data1} />
            <Table columns={columns} dataSource={data2} />

        </div>
    )
}

export default SupportAdmin