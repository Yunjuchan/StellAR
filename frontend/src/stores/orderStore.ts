import create from 'zustand';

interface OrderStoreType {
  isModalOpen: boolean;
  setIsModalOpen: (isOpen: boolean) => void;
  address: {
    postcode: string;
    address: string;
    extraAddress: string;
  };
  setAddress: (address: {
    postcode: string;
    address: string;
    extraAddress: string;
  }) => void;
}

const useOrderStore = create<OrderStoreType>((set, get) => ({
  isModalOpen: false,
  setIsModalOpen: (isOpen: boolean) => set({ isModalOpen: isOpen }),
  address: { postcode: '', address: '', extraAddress: '' },
  setAddress: (address) => set({ address: address }),
}));

export default useOrderStore;
