'use client';

import React, { useEffect, useState, Component } from 'react';
import backend_link from '@/links'

 
export default function Uploader() {
    const [backendResponse, setBackendResponse] = useState('\n');
    const [loading, setLoading] = useState(false);

    async function uploadFile (e) {
        setLoading(true);
        setBackendResponse('');
        const file = e.target.files[0];
        if (file != null) {
            const data = new FormData();
            data.append('file_from_react', file);

            let response = await fetch(backend_link + '/flask/upload',
            {
                method: 'post',
                body: data,
            });
            let res = await response.json();
            if (res.status !== 1){
                alert('Error uploading file');
            }else{
                setBackendResponse(res.result);
            }
            console.log(res.result)
        }
        setLoading(false);
    };
    
    if (loading){
        return (
        <div className="relative pt-32 pb-10 md:pt-40 md:pb-16">
            <div className="py-12 md:py-16">
                <div className="max-w-6xl mx-auto px-4 sm:px-6">
                    <h3 className="h3 mb-3">Loading...</h3>
                </div>
            </div>
        </div>
        );
    }else{
        const formattedResponse = backendResponse.replace(/\n/g, "<br>");
        return (
        <div className="relative pt-32 pb-10 md:pt-40 md:pb-16">
            <div className="py-12 md:py-16">
                <div className="max-w-6xl mx-auto px-4 sm:px-6">
                    <form>
                        <input className="btn text-white bg-green-600 hover:bg-green-700 w-full"
                            type="file"
                            onChange={uploadFile}>
                        </input>
                    </form>
                    <p className="text-xl text-gray-400 mb-4" dangerouslySetInnerHTML={{ __html: "Result: " + formattedResponse }}></p>
                </div>
            </div>
        </div>
        );
    }
};