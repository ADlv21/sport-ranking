import React from 'react';
import Link from 'next/link';
import { APP_NAME } from '@/lib/constants';
import Image from 'next/image';
import AppIcon from '@/assets/foot.png'
const Navbar = () => {
    return (
        <nav className="bg-gray-900 py-4 shadow-md">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">
                    <div className="flex items-center">
                        <Link href="/" className="flex text-white font-bold text-xl justify-center items-center space-x-4">
                            <Image
                                src={AppIcon}
                                className='w-14 rounded-full'
                            />
                            <span>{APP_NAME}</span>
                        </Link>
                    </div>
                    <div className="hidden md:block">
                        <div className="ml-10 flex items-baseline space-x-4">
                            <Link href="/sports" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">
                                Rankings
                            </Link>
                            <Link href="/contact" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">
                                Contact
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;