import Link from 'next/link';

const Navbar = () => {
    return (
        <nav className="bg-gray-800 p-4">
            <div className="container mx-auto flex justify-between items-center">
                <Link href="/" className="text-white text-2xl font-bold">
                    Your Logo
                </Link>
                <div className="space-x-4">
                    <Link href="/" className="text-white">
                        Home
                    </Link>
                    <Link href="/about" className="text-white">
                        About
                    </Link>
                    <Link href="/contact" className="text-white">
                        Contact
                    </Link>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;